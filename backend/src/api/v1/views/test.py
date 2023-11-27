from typing import List

from fastapi import APIRouter, Depends, Query

from common.registry import Registry
from src.api.v1.schemas.tests import FullTestResponseSchema, ShortTestResponseSchema
from src.api.v1.use_cases.test.get_single_test import GetSingleTestCase

router = APIRouter(tags=["Tests"])

@router.get("/tests/list", response_model=List[ShortTestResponseSchema])
def get_list_of_all_tests(
		get_tests_list_case = Depends(Registry.get_tests_list_case)
):
	"""Получение списка тестов
	note: может быть добавлен фильтр по классу и пагинация
	"""
	return get_tests_list_case()

@router.get("/tests", response_model=FullTestResponseSchema)
def get_list_of_all_tests(
		test_id: int = Query(...),
		get_test_case: GetSingleTestCase = Depends(Registry.get_single_test_case)
):
	"""Получение конкретного теста
	note: будет верификация по пользователю
	"""
	return get_test_case(test_id)
	