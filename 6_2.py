my_dict = {}

with open ('task.txt', encoding='utf-8') as t:
    for line in t:
        line = line.strip().split()
        my_dict[line[0]] = my_dict.get(line[0], 0) + 1
spamers = sorted(my_dict, key=my_dict.get, reverse=True)
print(f'Cпамер: {spamers[0]}, запросов: {my_dict.get(spamers[0])}')