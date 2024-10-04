def oraliq(n, minn, maxx):
    if not (minn <= n <= maxx):
        raise ValueError(f"Raqam {minn} va {maxx} oralig'ida bo'lishi kerak.")

m = input("Raqamni kiriting: ")

try:
    number = int(m)
    oraliq(number, 1, 100)
    print("Raqam to'g'ri.")
except ValueError as e:
    print(e)
