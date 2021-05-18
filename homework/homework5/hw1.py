import datetime


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

    def do_homework(self, homework_obj: Homework):
        if homework_obj.is_active():
            return homework_obj
        else:
            print('You are late')
            pass


class Teacher:
    """Info about teacher"""
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def create_homework(self, text: str, days_remaining: int) -> Homework:
        return Homework(text, days_remaining)
