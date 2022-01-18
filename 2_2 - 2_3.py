target = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(target))
i = 0
ln = len(target)
while i < ln:
    if target[i].isdigit() or target[i][1:].isdigit():
            target[i] = target[i].zfill(2)
            if target[i][0] in '+-':
                target[i] = target[i].zfill(3)
            target.insert(i, '"')
            target.insert(i + 2, '"')
            i += 2
            ln += 2
    i += 1
print(id(target))
print(target)
my_str = " ".join(target)
print(my_str)

