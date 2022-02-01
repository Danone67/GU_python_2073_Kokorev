from sys import argv

start_number = 1
end_number = float('inf')

if len(argv) == 2:
    start_number = int(argv[1])
elif len(argv) == 3:
    start_number = int(argv[1])
    end_number = int(argv[2])

with open('bakery.csv', encoding='utf-8') as b:
    idx = 1
    for line in b:
        if start_number <= idx <= end_number:
            print(line.strip())
        elif idx > end_number:
            break
        idx += 1