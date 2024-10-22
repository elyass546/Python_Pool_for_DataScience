def ft_filter(func, iterable):
    if func is None:
        return [item for item in iterable if item]
    else:
        return [item for item in iterable if func(item)]
