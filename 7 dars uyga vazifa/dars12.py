my_dict = {
    "ism": "Ali",
    "yosh": 30,
    "shahar": "Toshkent"
}

def get_value_from_dict(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        print(f"Kalit '{key}' topilmadi.")

search = input("Kalitni kiriting: ")

value = get_value_from_dict(my_dict, search)

if value is not None:
    print(f"{search} qiymati: {value}")
