users = {"nisse": "apa", "bosse": "ko", "stina": "t-rex"}

print("Användare:")
print()
for user in users:
    print(user)
print()

print("Användare och lösenord:")
print()
for user in users:
    print(f"{user}) {users[user]}")
print()

data = {"nisse": ["luva", "vante"], "bosse": ["spik", "skruv", "hammare"], "stina": ["tidsmaskin"]}

print("Användare och deras data:")
print()
for user in data:
    print(f"{user}) {data[user]}")
print()

user = input("Slå upp användare: ")
print()

if user in data:
    print(f"Data lagrat för {user}: {data[user]}")
else:
    print(f"Användaren {user} finns inte")
