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


def login(users):
    while True:
        user = input("User: ")
        password = input("Password: ")
        print()
        if user in users and users[user] == password:
            return user
        print("Invalid username or password")
        print()
        choice = menu("", "Option: ", {"r": "Try again", "q": "Quit"})
        if choice == "q":
            return None


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


def main():
    users = {"nisse": "apa", "stina": "t-rex", "bosse": "ko"}
    data = {"nisse": ["luva", "vante"], "stina": [], "bosse": ["gräs", "mjölk"]}

    option = menu("Welcome to Lagra (TM)", "Option: ", {"l": "Log in", "q": "Quit"})
    while option != "q":
        user = login(users)
        if user != None:
            user_actions(user, data[user])
        option = menu("Welcome to Lagra (TM)", "Option: ", {"l": "Log in", "q": "Quit"})


main()
