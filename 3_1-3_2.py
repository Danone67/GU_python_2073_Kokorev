translate = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(number):
    if number.istitle():
        number = number.lower()
        print(translate.get(number).title())
    else:
        print(translate.get(number))


num_translate_adv(input('Enter a number on English \n'))