i = 1
numbers = [i**3 for i in range(1, 1001, 2)]
print(numbers)
result = 0
for number in numbers:
    sum = 0
    item = number
    while item != 0:
        sum += item % 10
        item //= 10
    if not sum % 7:
        result += number
print(result)
result_2 = 0
for i in range(len(numbers)):
    numbers[i] += 17
print(numbers)
result = 0
for number in numbers:
    sum = 0
    item = number
    while item != 0:
        sum += item % 10
        item //= 10
    if not sum % 7:
        result += number
print(result)
#было сложно, но и интересно. сложно не столько в структуре программы, сколько в логике всех действий