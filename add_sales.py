import sys

with open('bakery.csv', 'a+', encoding='utf-8') as b:
    b.writelines(f'{sys.argv[1]}\n')