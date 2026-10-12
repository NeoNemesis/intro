users = {"nisse": "apa", "stina": "t-rex", "bosse": "ko"}

logged_in = False
while not logged_in:
    user = input("User: ")
    password = input("Password: ")
    print()
    if user in users and users[user] == password:
        logged_in = True
    else:
        print("Invalid username or password")
        print()

print(f"Welcome {user}")
