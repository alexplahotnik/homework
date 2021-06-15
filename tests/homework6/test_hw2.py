import pytest

from homework.homework6.hw2 import *

lazy_student = Student("Roman", "Petrov")
good_student = Student("Lev", "Sokolov")

opp_teacher = Teacher("Daniil", "Shadrin")
advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

oop_hw = opp_teacher.create_homework("Learn OOP", 1)
docs_hw = opp_teacher.create_homework("Read docs", 5)
dead_hw = advanced_python_teacher.create_homework("Make some noise", -2)

result_1 = good_student.do_homework(oop_hw, "I have done this hw")
result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
result_3 = lazy_student.do_homework(docs_hw, "done")


def test_exception_do_homework():
    with pytest.raises(AttributeError):
        lazy_student.do_homework(result_1, "done")
    with pytest.raises(DeadlineError):
        lazy_student.do_homework(dead_hw, "done")


def test_homework_done_dict():
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2


def test_reset_homework_done():
    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)
    assert Teacher.homework_done
    Teacher.reset_results()
    assert not Teacher.homework_done
