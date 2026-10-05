from random import randint

open = 0
closed = 1


def splash():
    print()
    print("--------------------------------")
    print("Biathlon")
    print()
    print("a hit or miss game")
    print("--------------------------------")
    print()


def is_open(value):
    return value == open


def is_closed(value):
    return value == closed


def new_targets():
    targets = []
    for i in range(5):
        targets.append(open)
    return targets


def close_target(targets, position):
    targets[position] = closed
    return targets


def points(targets):
    n = 0
    for target in targets:
        if is_closed(target):
            n = n + 1
    return n


def target_to_string(target):
    if is_open(target):
        return "*"
    else:
        return "O"


def targets_to_string(targets):
    text = ""
    for target in targets:
        text = text + target_to_string(target) + " "
    return text


def view_targets(targets):
    print()
    print("1 2 3 4 5")
    print()
    print(targets_to_string(targets))
    print()


def random_hit():
    return randint(0, 1) == 1


def shoot(targets, position):
    if random_hit():
        if is_open(targets[position]):
            close_target(targets, position)
            return "Hit on open target"
        else:
            return "Hit on closed target"
    else:
        return "Miss"


def parse_target(string):
    if string in ["1", "2", "3", "4", "5"]:
        return int(string) - 1
    return None


def play():
    splash()
    print("Write a number 1 - 5 to choose a target and press Enter.")
    print()
    print("You got 5 shots")
    targets = new_targets()
    view_targets(targets)

    for shot in range(1, 6):
        position = parse_target(input("Shot nr " + str(shot) + " at: "))
        while position == None:
            position = parse_target(input("Write 1 - 5: "))
        print()
        print(shoot(targets, position))
        view_targets(targets)

    print("You hit " + str(points(targets)) + " of 5 targets")


play()
