import os
import re
from dataclasses import dataclass

INPUT_FILE = "input"

with open(f"{os.path.dirname(__file__)}/{INPUT_FILE}", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]


@dataclass(frozen=True, slots=True)
class Card:
    id: int
    winning: set[int]
    actual: set[int]


def parse_card(line: str) -> Card:
    match = re.search(r'Card +(\d+): +(.+) +\| +(.+)', line)
    id_str, winning_str, actual_str = match.groups()
    winning = {int(n) for n in winning_str.split(' ') if n}
    actual = {int(n) for n in actual_str.split(' ') if n}
    return Card(int(id_str), winning, actual)


def get_card_value(card: Card) -> int:
    combination = card.actual & card.winning
    if len(combination) == 0:
        return 0
    return int(2**(len(combination) - 1))



cards = [parse_card(line) for line in input_]
answer = sum(map(lambda c: get_card_value(c), cards))
print(answer)
