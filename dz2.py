numbers = []
i = 1
while i <= 1000:
    if i % 2:
        i = i ** 3
        numbers.append(i)
        i += 1
print(numbers)
