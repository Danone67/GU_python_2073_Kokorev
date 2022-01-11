dur = int(input(' Введите количество секунд - '))
min = dur // 60
sec = dur % 60
hours = min // 60
days = hours // 24

if 1 <= min < 60:
    print(min, 'мин', sec, 'сек')
elif min >= 60:
    minute = min % 60
    if hours < 24:
        print(hours, 'ч', minute, 'м', sec, 'с')
    elif hours >= 24:
        days = hours // 24
        hhours = hours % 24
        print(days, 'дн', hhours, 'ч', minute, 'мин', sec, 'сек')
else:
    print(sec, 'сек')
