def odd_nums_adv(n):
    nums_comp = [n for n in range(1, n + 1, 2)]
    print(*nums_comp)

odd_nums_adv(int(input('Введите количество чисел в последовательности: ')))