"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict


class DeadlineError(Exception):
    pass


class Homework:
    """Info about your homework"""

    def __init__(self, text: str, days_remaining: int):
        self.text = text
        self.deadline = datetime.timedelta(days=days_remaining)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        time_remaining = self.created + self.deadline - datetime.datetime.now()
        return time_remaining.total_seconds() > 0


class Student:
    """Info about student"""

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, homework_obj: Homework, solution):
        try:
            if homework_obj.is_active():
                return HomeworkResult(self, homework_obj, solution)
            else:
                raise DeadlineError("You are late")
        except AttributeError:
            raise AttributeError("You gave a not Homework object")


class Teacher(Student):
    """Info about teacher"""

    homework_done = defaultdict(set)

    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)

    def create_homework(self, text: str, days_remaining: int) -> Homework:
        return Homework(text, days_remaining)

    @classmethod
    def check_homework(cls, homework_result_obj):
        if len(homework_result_obj.solution) > 5:
            cls.homework_done[homework_result_obj.homework].add(homework_result_obj)
            return True
        else:
            return False

    @classmethod
    def reset_results(cls, homework=None):
        if type(homework) == Homework:
            del cls.homework_done[homework]
        if not homework:
            cls.homework_done = defaultdict(set)


class HomeworkResult:
    def __init__(self, author: Student, homework: Homework, solution):
        self.author = author
        self.homework = homework
        self.solution = solution
        self.created = homework.created
