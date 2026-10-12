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


strings = []
n = 5

print(f"n = {n}")
print()

while len(strings) < n:
    add("Lägg till en sträng: ", strings)
    print()

view(f"Du har matat in följande {n} strängar", strings)
