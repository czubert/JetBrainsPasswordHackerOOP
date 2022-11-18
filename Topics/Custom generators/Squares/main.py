n = int(input())


def squares(x):
    i = 1
    while i <= x:
        yield i ** 2
        i += 1


my_gen = squares(n)

for num in my_gen:
    print(num)
# Don't forget to print out the first n numbers one by one here
