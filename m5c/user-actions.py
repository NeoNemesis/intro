def add(prompt, strings):
    string = input(prompt)
    strings.append(string)
    return strings


def view(description, strings):
    print(description)
    print()
    number = 1
    for string in strings:
        print(f"{number}) {string}")
        number = number + 1


def menu(title, prompt, options):
    if title != "":
        print(title)
        print()
    for option in options:
        print(f"{option}) {options[option]}")
    print()

    option = input(prompt)
    while option not in options:
        option = input(prompt)

    print()
    return option


def user_actions(user, items):
    print(f"Welcome {user}")
    print()
    view("These are your items", items)
    print()

    options = {"a": "Add item", "l": "List items", "q": "Log out"}
    option = menu("Select an action", "Option: ", options)
    while option != "q":
        if option == "a":
            add("Add item: ", items)
            print()
        view("These are your items", items)
        print()
        option = menu("Select an action", "Option: ", options)

    return items


user1 = "nisse"
user2 = "bosse"

items1 = ["luva", "vante"]
items2 = ["hammare", "skruv", "spik"]

user_actions(user1, items1)
print(f"Goodbye {user1}, your items: {items1}")
print()

user_actions(user2, items2)
print(f"Goodbye {user2}, your items: {items2}")
print()
