import json
def minmax(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)

        ages = [user["yosh"] for user in data if "yosh" in user]
        
        if ages:
            print(f"Eng katta yosh: {max(ages)}")
            print(f"Eng kichik yosh: {min(ages)}")
        else:
            print("Yosh ma'lumotlari topilmadi.")
    except FileNotFoundError:
        print("Fayl topilmadi.")

