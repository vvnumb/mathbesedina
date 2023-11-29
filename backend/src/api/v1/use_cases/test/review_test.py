import logging
from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List, Set, Tuple

from common.orm.models.enums import TaskType
from common.service_interface import SyncService
from src.api.v1.schemas.dtos.done_test import DoneTestDTOSchema, _ResolvedTask
from src.api.v1.schemas.tests import ReviewedTestSchema
from src.infrastructure.unit_of_work.test import TestUnitOfWork
from src.models import Task, TaskAnswer


@dataclass(slots=True, frozen=True, kw_only=True)
class ReviewTestCase(SyncService):
	uow: TestUnitOfWork
	
	def __call__(self, resolved_test: DoneTestDTOSchema) -> ReviewedTestSchema:
		tasks: List[_ResolvedTask] = resolved_test.root
		task_ids: Set[int] = {taks.id for taks in tasks}
		
		with self.uow:
			right_answers: List[TaskAnswer] = self.uow.answers.get_list(
				TaskAnswer.task_id.in_(task_ids),
				TaskAnswer.is_right == True
			)
		
		mapped_right_answers: Dict[int, List[TaskAnswer]] = defaultdict(list)  # todo: drop here
		
		for answer in right_answers:
			task_id = answer.task_id
			mapped_right_answers[task_id] += [answer]
		
		right_answers_count: int = 0
		
		for done_task in tasks:
			done_answers = done_task.answer
			if done_answers is None:
				continue
			if not isinstance(done_answers, list):
				done_answers = [done_answers]
			
			right_answers: List[TaskAnswer] = mapped_right_answers[done_task.id]
			
			if len(done_answers) != len(right_answers):
				continue
			
			is_correct = self.__check_answer(done_task, done_answers, right_answers)
			right_answers_count += int(is_correct)
			
		# note: len(tasks) может содержать не все задачи теста
		return ReviewedTestSchema(correct_answers=right_answers_count)
	
	def __check_answer(self, task, done_answers, right_answers) -> bool:
		is_correct: bool = False
		if task.task_type is TaskType.SINGLE:
			is_correct = \
				len(done_answers) == 1 and int(done_answers[0]) == right_answers[0].id
		elif task.task_type is TaskType.FULL:
			is_correct = \
				len(done_answers) == 1 and done_answers[0] == right_answers[0].title
		elif task.task_type is TaskType.MANY:
			is_correct = \
				set(map(int, done_answers)) == set(answer.id for answer in right_answers)
		else:
			logging.warning("Unknown task type accured")
		return is_correct
			