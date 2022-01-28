from collections import Counter

#в лоб
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [i for i in src if src.count(i) == 1]
print(result)
#другой вариант
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
used = set()
unique = [x for x in src if x not in used and (used.add(x) or True)]

counter = Counter(src)
unique = list(counter)

single = [x for x, n in counter.items() if n == 1]
print(single)
