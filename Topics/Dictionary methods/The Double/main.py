# put your python code here
import string
alph = list(string.ascii_lowercase)
double = [2 * x for x in alph]

double_alphabet = dict.fromkeys(alph)

for el in double:
    alpa_key = el[0]
    double_alphabet[alpa_key] = el
