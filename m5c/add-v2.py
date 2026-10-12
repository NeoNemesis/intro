# Definition of the function add.


def add(prompt, strings):
    string = input(prompt)
    strings.append(string)
    return strings


# Test of the function add with the list ducks.

ducks = ["Huey", "Dewey", "Louie"]

print(f"Ducks: {ducks}")
print()

add("Add a duck: ", ducks)

print(f"Ducks: {ducks}")
print()

add("Add a duck: ", ducks)

print(f"Ducks: {ducks}")
print()

# Test of the function add with the list composers.

composers = ["Mozart", "Bach"]
print(f"Composers: {composers}")
print()

add("Add a composer: ", composers)

print(f"Composers: {composers}")
print()
