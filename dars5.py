fayl = '2fayl.txt'
yangi = 'natija.txt'

with open(fayl, 'r') as file:
    satrlar = file.readlines()

with open(yangi, 'w') as file:
    for satr in satrlar:
        file.write(satr[::-1])

print(f"'{yangi}' fayliga teskari yozildi.")
