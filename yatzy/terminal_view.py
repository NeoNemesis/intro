from game import MAX_PLAYERS, MIN_PLAYERS, NUM_DICE, Game
from scoring import CATEGORIES, UPPER, category_name

# Vilka prickar som syns på varje sida, rad för rad
PIPS = {
    1: ["       ", "   o   ", "       "],
    2: [" o     ", "       ", "     o "],
    3: [" o     ", "   o   ", "     o "],
    4: [" o   o ", "       ", " o   o "],
    5: [" o   o ", "   o   ", " o   o "],
    6: [" o   o ", " o   o ", " o   o "],
}

NAME_WIDTH = 8


def dice_lines(values, held):
    lines = ["", "", "", "", "", "", ""]
    for i in range(len(values)):
        pips = PIPS[values[i]]
        lines[0] += "+-------+  "
        lines[1] += f"|{pips[0]}|  "
        lines[2] += f"|{pips[1]}|  "
        lines[3] += f"|{pips[2]}|  "
        lines[4] += "+-------+  "
        lines[5] += f"    {i + 1}      "
        lines[6] += " SPARAD    " if held[i] else "           "
    return lines


def show_dice(dice):
    print()
    for line in dice_lines(dice.values, dice.held):
        print(line.rstrip())


def show_scorecard(game):
    names = [player.name[:NAME_WIDTH] for player in game.players]
    header = "".ljust(14) + "".join(name.rjust(NAME_WIDTH + 1) for name in names)
    print()
    print(header)
    print("-" * len(header))

    for key, name in CATEGORIES:
        row = name.ljust(14)
        for player in game.players:
            value = player.scores.get(key)
            cell = "-" if value is None else str(value)
            row += cell.rjust(NAME_WIDTH + 1)
        print(row)
        if key == UPPER[-1]:
            print_sum_row("Summa", [p.upper_sum() for p in game.players])
            print_sum_row("Bonus", [p.bonus() for p in game.players])
            print("-" * len(header))

    print("-" * len(header))
    print_sum_row("Totalt", [p.total() for p in game.players])


def print_sum_row(label, values):
    row = label.ljust(14)
    for value in values:
        row += str(value).rjust(NAME_WIDTH + 1)
    print(row)


def ask_players():
    while True:
        answer = input(f"Hur många spelare? ({MIN_PLAYERS}-{MAX_PLAYERS}): ").strip()
        if answer.isdigit() and MIN_PLAYERS <= int(answer) <= MAX_PLAYERS:
            break
        print(f"Skriv ett tal mellan {MIN_PLAYERS} och {MAX_PLAYERS}.")

    names = []
    for i in range(int(answer)):
        name = input(f"Namn på spelare {i + 1}: ").strip()
        if name == "":
            name = f"Spelare {i + 1}"
        names.append(name)
    return names


def parse_positions(answer):
    positions = []
    for char in answer.replace(",", " ").replace(" ", ""):
        if not char.isdigit() or not 1 <= int(char) <= NUM_DICE:
            return None
        positions.append(int(char) - 1)
    return positions


def ask_keep_or_score(game):
    while True:
        print()
        print(f"Slag kvar: {game.rolls_left}")
        print("Skriv numren på tärningarna du vill spara (t.ex. 135)")
        print("Enter = slå om alla, p = sätt poäng, v = visa protokollet")
        answer = input("> ").strip().lower()

        if answer == "p":
            return "score"
        if answer == "v":
            show_scorecard(game)
            show_dice(game.dice)
            continue

        positions = parse_positions(answer)
        if positions is None:
            print(f"Ogiltigt val. Använd siffrorna 1-{NUM_DICE}.")
            continue
        game.dice.hold_only(positions)
        return "roll"


def ask_category(game):
    available = game.available_categories()
    print()
    print("Välj var du vill sätta poängen:")
    for i in range(len(available)):
        key = available[i]
        print(f"  {i + 1:2}. {category_name(key):<12} {game.preview(key):>3} p")

    while True:
        answer = input("> ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(available):
            return available[int(answer) - 1]
        print(f"Skriv ett tal mellan 1 och {len(available)}.")


def play_turn(game):
    player = game.current_player()
    print()
    print("=" * 40)
    print(f"{player.name}s tur")
    print("=" * 40)
    input("Tryck enter för att slå tärningarna...")

    game.roll()
    show_dice(game.dice)
    while game.can_roll():
        if ask_keep_or_score(game) == "score":
            break
        game.roll()
        show_dice(game.dice)

    category = ask_category(game)
    points = game.choose(category)
    print(f"{player.name} fick {points} p på {category_name(category)}.")


def show_result(game):
    show_scorecard(game)
    print()
    winners = game.winners()
    if len(winners) == 1:
        print(f"{winners[0].name} vann med {winners[0].total()} poäng!")
    else:
        names = " och ".join(player.name for player in winners)
        print(f"Oavgjort mellan {names} med {winners[0].total()} poäng!")


def splash():
    print()
    print("--------------------------------")
    print("Yatzy")
    print()
    print(f"för {MIN_PLAYERS}-{MAX_PLAYERS} spelare")
    print("--------------------------------")
    print()


def run():
    splash()
    game = Game(ask_players())
    while not game.is_over():
        play_turn(game)
        if game.current == 0 and not game.is_over():
            show_scorecard(game)
    show_result(game)
