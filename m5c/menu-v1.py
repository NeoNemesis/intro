options = {"a": "Add item", "l": "List items", "q": "Log out"}

print("Select an action")
print()
for option in options:
    print(f"{option}) {options[option]}")
print()

option = input("Option: ")
while option not in options:
    option = input("Option: ")

print()
print(f"You selected option {option}) {options[option]}")
