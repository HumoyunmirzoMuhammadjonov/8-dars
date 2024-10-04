import random 

fayl = 'random.txt'
new = 'juft.txt'

with open(fayl, 'w') as file:
    for _ in range(20):
        raqam = random.randint(1, 100)
        file.write(f"{raqam}\n")

with open(fayl, 'r') as file:
    raqamlar = [int(satr.strip()) for satr in file.readlines()]

with open(fayl, 'w') as file:
    for raqam in raqamlar:
        if raqam % 2 == 0:
            file.write(f"{raqam}\n")

print(f"Juft raqamlar '{fayl}' fayliga yozildi.")