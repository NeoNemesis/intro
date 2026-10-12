def login(users):
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
    return user


users1 = {"nisse": "apa", "stina": "t-rex", "bosse": "ko"}
user1 = login(users1)
print(f"Welcome {user1}")
print()

users2 = {"foo": "123", "bar": "hello", "foobar": "hello123"}
user2 = login(users2)
print(f"Welcome {user2}")
