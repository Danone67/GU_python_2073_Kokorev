def odd_nums(n):
    for i in range(1, n + 1, 2):
        yield i

#print(*odd_nums(10), sep=' ')

odd_to_15 = odd_nums(15)

print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))