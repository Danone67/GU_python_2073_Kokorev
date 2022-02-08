from functools import wraps


def val_checker(validator):
    def _val_checker(func):
        @wraps(func)
        def wrapper_logger(*args):
            result = func(*args)
            if not validator(*args):
                raise ValueError(f'Wrong val {args[0]}')

            return result

        return wrapper_logger

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(f'{calc_cube(3)} {calc_cube.__name__}')
# print(calc_cube(-3))
