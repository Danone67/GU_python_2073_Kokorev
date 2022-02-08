import re


def email_parse(address):
    valid = re.compile(r"^[-\w.]+@([-\w]+\.)+[-\w]{2,4}$")  # минимальная проверка валидности адреса, до парсинга
    valid_add = valid.match(address)
    if not valid_add:
        raise ValueError(f'Адрес {address} не валиден')
    pattern = re.compile(r'^(?P<username>\w+)@(?P<domain>\w+\.\w+)$')
    res = pattern.match(address)
    return res.groupdict()


print(email_parse(input('Введите email адрес - ')))
