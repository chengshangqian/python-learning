import json


def get_stored_username():
    try:
        filename = "username.json"
        with open(filename) as file:
            username = json.load(file)
    except FileNotFoundError:
        print("username.json file not found.")
        return None
    else:
        return username


def get_new_username():
    filename = "username.json"
    username = input("What's your name? ")
    with open(filename, "w") as file:
        json.dump(username, file)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + ".")


greet_user()
