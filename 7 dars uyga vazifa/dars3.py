import os

fayl = '2fayl.txt'

if os.path.exists(fayl):
    with open(fayl, 'r') as file:
        m = file.read()
        n = m.split()
        word = len(n)
    print(f"'{fayl}' faylida {word} ta so'z bor.")
else:
    print(f"'{fayl}' fayli topilmadi.")
