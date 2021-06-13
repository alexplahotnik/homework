from contextlib import contextmanager


class SuppressorClass:
    """Context manager, that suppress all exceptions"""

    def __init__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True


@contextmanager
def suppressor_function():
    """Function, that suppress all exceptions"""
    try:
        yield
    finally:
        return True
