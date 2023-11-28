from typing import List, Union

from pydantic import BaseModel, RootModel, model_validator

from common.orm.models.enums import TaskType


class _ResolvedTask(BaseModel):
	id: int
	task_type: TaskType
	answer: Union[str, int, List[int]]
	
	@model_validator(mode='before')
	@classmethod
	def answer_to_int(cls, data: dict) -> dict:
		task_type = data["task_type"]
		if task_type == TaskType.SINGLE:
			data["answer"] = int(data["answer"])
		
		return data

class DoneTestDTOSchema(RootModel):
	root: List[_ResolvedTask]
