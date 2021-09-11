def describe_pet(type, name):
    print("I have a " + type.lower())
    print("It's name is " + name.title())


def desc_pet(name, type="dog"):
    print("I have a " + type.lower() + ", it's name is " + name.title())


describe_pet("dog", "harry")
describe_pet(type="hamster", name="Lucky")
describe_pet(name="nuomy", type="Cat")
desc_pet("Jerry", type="Cat")

