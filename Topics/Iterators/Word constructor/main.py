first_word = input()
second_word = input()

for char1, char2 in zip(first_word, second_word):
    print(char1 + char2, end='')
