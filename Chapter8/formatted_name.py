def get_formatted_name(first_name, middle_name, last_name):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


full_name = get_formatted_name("Cheng", None, "qian")
print(full_name)
full_name = get_formatted_name("Cheng", "", "qian")
print(full_name)
full_name = get_formatted_name("Cheng", "Shang", "qian")
print(full_name)