n = int(input())


def even(x):
    i = 0
    while i <= x * 2 - 2:
        if i % 2 == 0:
            yield i
        i += 1


my_generator = even(n)

for el in my_generator:
    print(el)
