import itertools

# flower_names = ['rose', 'tulip', 'sunflower', 'daisy']

for i in range(1, 4):
    for el in itertools.combinations(flower_names, i):
        print(el)
