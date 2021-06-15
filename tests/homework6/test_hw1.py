import pytest

from homework.homework6.hw1 import instances_counter


def test_methods():
    @instances_counter
    class User:
        pass

    assert User.get_created_instances() == 0
    user, _, _ = User(), User(), User()
    assert User.get_created_instances() == 3
    assert User.reset_instances_counter() == 3
    assert User.get_created_instances() == 0
    new_user = User()
    assert User.get_created_instances() == 1
