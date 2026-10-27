from collections import Counter

# Kategorierna i den ordning de står i protokollet: (nyckel, namn)
CATEGORIES = [
    ("ettor", "Ettor"),
    ("tvaor", "Tvåor"),
    ("treor", "Treor"),
    ("fyror", "Fyror"),
    ("femmor", "Femmor"),
    ("sexor", "Sexor"),
    ("ett_par", "Ett par"),
    ("tva_par", "Två par"),
    ("tretal", "Tretal"),
    ("fyrtal", "Fyrtal"),
    ("liten_stege", "Liten stege"),
    ("stor_stege", "Stor stege"),
    ("kak", "Kåk"),
    ("chans", "Chans"),
    ("yatzy", "Yatzy"),
]

UPPER = ["ettor", "tvaor", "treor", "fyror", "femmor", "sexor"]

BONUS_LIMIT = 63
BONUS_POINTS = 50
YATZY_POINTS = 50


def category_name(category):
    for key, name in CATEGORIES:
        if key == category:
            return name
    raise ValueError(f"Okänd kategori: {category}")


def faces_with_at_least(counts, n):
    return [face for face, count in counts.items() if count >= n]


def score(category, values):
    counts = Counter(values)

    if category in UPPER:
        face = UPPER.index(category) + 1
        return face * counts[face]

    if category == "ett_par":
        pairs = faces_with_at_least(counts, 2)
        return 2 * max(pairs) if pairs else 0

    if category == "tva_par":
        pairs = faces_with_at_least(counts, 2)
        return 2 * sum(pairs) if len(pairs) == 2 else 0

    if category == "tretal":
        triples = faces_with_at_least(counts, 3)
        return 3 * triples[0] if triples else 0

    if category == "fyrtal":
        quads = faces_with_at_least(counts, 4)
        return 4 * quads[0] if quads else 0

    if category == "liten_stege":
        return 15 if sorted(values) == [1, 2, 3, 4, 5] else 0

    if category == "stor_stege":
        return 20 if sorted(values) == [2, 3, 4, 5, 6] else 0

    if category == "kak":
        return sum(values) if sorted(counts.values()) == [2, 3] else 0

    if category == "chans":
        return sum(values)

    if category == "yatzy":
        return YATZY_POINTS if len(counts) == 1 else 0

    raise ValueError(f"Okänd kategori: {category}")
