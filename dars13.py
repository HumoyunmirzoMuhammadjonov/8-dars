def harflar(s):
    if not s.isalpha():
        raise ValueError("String faqat harflardan iborat bo'lishi kerak.")

m = input("Stringni kiriting: ")

try:
    harflar(m)
    print("Kiritilgan string to'g'ri.")
except ValueError as e:
    print(e)
