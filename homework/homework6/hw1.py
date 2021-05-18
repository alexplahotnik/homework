"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""
import types


def instances_counter(original_cls):
    """Decorator, that adds new methods to original class"""

    class WrappedClass(original_cls):
        i = 0

        @classmethod
        def __init__(cls):
            cls.i += 1

        @classmethod
        def get_created_instances(cls):
            """Return count of created instances"""
            return cls.i

        @classmethod
        def reset_instances_counter(cls):
            """Return count of created instances and reset it"""
            copy = cls.i
            cls.i = 0
            return copy

    return WrappedClass
