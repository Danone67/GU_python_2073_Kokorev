import os

root_dir = input('Введите путь к папке - ')

num_gen = {10**i: 0 for i in range(2, 6)}

for root, dirs, files in os.walk(root_dir):
    for file in os.scandir(root):
        for num in num_gen:
            if file.stat().st_size < num:
                num_gen[num] += 1
                break

print(num_gen)