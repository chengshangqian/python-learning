try:
    filename = "it_is_not_a_file.txt"
    with open(filename) as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    # pass表示跳过,即失败时直接跳过
    # pass
    print("file " + filename + " is not found.")