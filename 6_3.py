import json
from itertools import zip_longest

with open('users.csv', encoding='utf-8') as u, open('hobby.csv', encoding='utf-8') as h, \
        open('user_hobby.json', 'w', encoding='utf-8') as f:
    if len(list(u)) < len(list(h)):
        exit(1)
    u.seek(0)
    h.seek(0)
    my_dict = {}
    for line_u, line_h in zip_longest(u, h):
        my_dict[line_u.strip().replace(',', ' ')] = line_h.strip() if line_h is not None else line_h
    json.dump(my_dict, f)

with open('user_hobby.json', encoding='utf-8') as f:
    our_dict = json.load(f)
print(our_dict)
