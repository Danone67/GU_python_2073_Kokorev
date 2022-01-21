from random import choice
from pprint import pprint


def get_jokes(n: int, not_repeat: bool = False) -> list:
    """
    Возвращает n случайно сгенерированных шуток
    :param n: количество шуток
    :param not_repeat: Если True - уникальные шутки, если False - нет
    :return: список шуток
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    result = []
    idx = 0

    while idx < n:
        my_noun = choice(nouns)
        my_adv = choice(adverbs)
        my_adj = choice(adjectives)
        if not_repeat:
            nouns.remove(my_noun)
            adverbs.remove(my_adv)
            adjectives.remove(my_adj)
            if n > 5:
                print('Уникальных может быть только 5 :( ')
                break
        result.append(f'{my_noun} {my_adv} {my_adj}')
        idx += 1
    return result


pprint(get_jokes(int(input('Введите количество шуток ')), not_repeat=True))