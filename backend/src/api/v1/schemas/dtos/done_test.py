from typing import List, Union

from pydantic import BaseModel, RootModel, ValidationError, model_validator

from common.orm.models.enums import TaskType


class _ResolvedTask(BaseModel):
	id: int
	task_type: TaskType
	answer: Union[str, int, List[int], None]
	
	@model_validator(mode='before')
	@classmethod
	def answer_to_int(cls, data: dict) -> dict:
		task_type = data["task_type"]
		answer = data["answer"]
		
		if answer is None:
			raise ValidationError.from_exception_data("Answer wanst done", line_errors=[])
		
		try:
			if task_type == TaskType.SINGLE:
				data["answer"] = int(answer)
			elif task_type == TaskType.MANY:
				if not isinstance(answer, list):
					raise TypeError
			elif task_type == TaskType.FULL:
				data["answer"] = str(answer)
		except TypeError as te:
			raise ValidationError.from_exception_data("Bad answer", line_errors=[])
		
		return data

class DoneTestDTOSchema(RootModel):
	root: List[_ResolvedTask]
