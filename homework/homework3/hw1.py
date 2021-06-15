def decorator_cache_maker(times):
    def decorator_cache(func):
        cash = {}
        times_remaining = times + 1

        def wrapped_cash_func(*args, **kwargs):
            nonlocal cash, times_remaining
            key = hash((args, tuple(kwargs)))
            if not cash.get(key):
                cash[key] = func(*args, **kwargs)
            elif times_remaining:
                times_remaining -= 1
            if not times_remaining:
                cash = {}
                cash[key] = func(*args, **kwargs)
            return cash[key]

        return wrapped_cash_func

    return decorator_cache
