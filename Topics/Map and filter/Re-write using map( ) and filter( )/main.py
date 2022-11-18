even = [0, 2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# Re-write the rest of the code here using map() and filter() where possible
my_sum = list(map(lambda x, y: x + y, even, odd))

remainders = list(map(lambda x: x % 3, my_sum))

nonzero_remainders = list(filter(lambda x: x != 0, remainders))