import json


with open("dars7.json", "r") as f:
    d = json.load(f)


d["yosh"] = 25

with open("dars7.json", "w") as f:
    json.dump(d, f)

print("JSON fayli yangilandi.")