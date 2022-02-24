from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            print(f'{calc_cube.__name__}({arg}: {type(arg)})', end='\n')
        return func(*args)

    return wrapper


@type_logger
def calc_cube(*args):
    return tuple(map(lambda x: x ** 3, args))


a = calc_cube(5, 6)
print(a)
