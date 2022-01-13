dur = int(input(' Введите количество секунд - '))
min = dur // 60
sec = dur % 60
hours = min // 60
days = hours // 24

if 1 <= min < 60:
    print(min, 'мин', sec, 'сек')
elif min >= 60:
    minutes = min % 60
    if hours < 24:
        print(hours, 'ч', minutes, 'м', sec, 'с')
    elif hours >= 24:
        days = hours // 24
        Hours = hours % 24
        print(days, 'дн', Hours, 'ч', minutes, 'мин', sec, 'сек')
else:
    print(sec, 'сек')
