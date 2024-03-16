import json
user = {
    "Me":{
        "User_ID": int(),
        "User_Name": str(),
        "User_password": str(),
        "User_frase": str(),
        "User_about": str(),
        "User_happy_birthday": {
            "birthday_day": int(),
            "birthday_moon": int(),
            "birthday_year": int()
        }}
}

with open("JSON\\user_info.json", "w") as file:
    json.dump(user, file, sort_keys=True)

with open('JSON\\user_info.json', 'r') as file:
    settings = json.load(file)