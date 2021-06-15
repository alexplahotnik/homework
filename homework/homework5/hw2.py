import functools


def my_decorator(wrapped):
    def update_wrapper(wrapper):
        wrapper.__name__ = wrapped.__name__
        wrapper.__doc__ = wrapped.__doc__
        wrapper.__original_func = wrapped
        return wrapper

    return update_wrapper


def print_result(func):
    @my_decorator(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)
