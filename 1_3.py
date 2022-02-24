percent = int(input('Введите количество процентов - '))
single = (1, 21, 31, 41, 51, 61, 71, 81, 91)
letter_a = (2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94)
if percent in single:
    print(percent, ' процент')
elif percent in letter_a:
    print(percent, ' процента')
else: print(percent, ' процентов')
print('Проверка')
results = list(range(1, 101))
idx = 1
while idx < len(results):
    if idx in single:
        print(idx, ' процент')
    elif idx in letter_a:
        print(idx, ' процента')
    else:
        print(idx, ' процентов')
    idx += 1