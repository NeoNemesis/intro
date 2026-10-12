def view(description, strings):
    print(description)
    print()
    number = 1
    for string in strings:
        print(f"{number}) {string}")
        number = number + 1


names = ["nisse", "stina", "bosse", "mimmi"]
animals = ["giraff", "myrslok", "tapir"]

view("Lista med namn", names)
print()
view("Lista med djur", animals)
