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


users = {"nisse": "apa", "stina": "t-rex", "bosse": "ko"}

user = login(users)
