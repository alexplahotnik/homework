import pytest

from homework.homework5.hw1 import *


@pytest.fixture()
def start_attr():
    my_homework = Homework("Kill your cat", 4)
    me = Student("Aleksandr", "Plakhotnik")
    my_teacher = Teacher("Denis", "Timofeev")
    return (my_homework, me, my_teacher)


def test_homework_is_active(start_attr):
    assert start_attr[0].is_active()


def test_homework_is_lost(start_attr):
    start_attr[0].deadline = datetime.timedelta(0)
    assert not start_attr[0].is_active()


def test_student_have_time(start_attr):
    assert start_attr[1].do_homework(start_attr[0]) == start_attr[0]


def test_student_is_late(start_attr):
    start_attr[0].deadline = datetime.timedelta(-1)
    assert not start_attr[1].do_homework(start_attr[0])


def test_teachers_homework(start_attr):
    assert start_attr[2].create_homework("Kill your cat", 4).is_active()
