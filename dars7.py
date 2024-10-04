import json

d = {
    "ism": "ali",
    "yosh": 23
}

with open("dars7.json", "w") as f:
    json.dump(d, f)

