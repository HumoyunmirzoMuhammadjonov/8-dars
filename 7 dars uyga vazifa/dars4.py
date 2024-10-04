fayl = '2fayl.txt'

with open(fayl, 'r') as file:
    m = file.read()
    sozlar = m.split()

if sozlar:
    minn = min(sozlar, key=len)
    maxx = max(sozlar, key=len)
    print(f"Qisqa so'z: '{minn}'\nUzun so'z: '{maxx}'")
else:
    print("Fayl bo'sh.")
