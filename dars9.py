import json

# Faylni o'qishga harakat qilamiz
try:
    with open("dars8.json", "r") as f:
        data = json.load(f)

    # Foydalanuvchilar orasidan yoshlarni ajratamiz
    ages = [user.get("yosh") for user in data if "yosh" in user]

    # Eng katta va eng kichik yoshni topamiz
    if ages:
        max_age = max(ages)
        min_age = min(ages)
        print(f"Eng katta yosh: {max_age}")
        print(f"Eng kichik yosh: {min_age}")
    else:
        print("Yosh ma'lumotlari topilmadi.")

except FileNotFoundError:
    print("Fayl topilmadi.")
