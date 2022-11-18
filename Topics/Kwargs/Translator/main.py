def translate(**kwargs):
    for eng, spa in kwargs.items():
        print(eng, ":", spa)


words = {"mother": "madre", "father": "padre",
         "grandmother": "abuela", "grandfather": "abuelo"}

translate(**words)
