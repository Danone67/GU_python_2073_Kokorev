from itertools import zip_longest, islice
import sys

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Даниил', 'Константин'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

#вариант 1

pupils = ((tutors[i], klasses[i]) if i < len(klasses) else (tutors[i], None) for i in range(len(tutors)))

print(type(pupils))

print(*pupils)

print(sys.getsizeof(pupils))
#вариант 2

pupils_2 = ((tutors, klasses) for tutors, klasses in zip_longest(tutors, klasses))

print(*pupils_2)

print(next(pupils_2, 'Истощился'))