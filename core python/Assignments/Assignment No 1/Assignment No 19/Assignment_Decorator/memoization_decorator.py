def memoize(fun):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = fun(*args)
        cache[args] = result
        return result
    
    return wrapper
