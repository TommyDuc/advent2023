from collections import defaultdict
import os
import re
from dataclasses import dataclass, field

INPUT_FILE = "input"

with open(f"{os.path.dirname(__file__)}/{INPUT_FILE}", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]


@dataclass(slots=True)
class Card:
    id: int
    winning: set[int]
    actual: set[int]
    original_value: int
    combination: set[int]
    copies: list["Card"] = field(default_factory=list)
    
    @property
    def is_winning(self) -> bool:
        return len(self.combination) == 0


def parse_card(line: str) -> Card:
    match = re.search(r'Card +(\d+): +(.+) +\| +(.+)', line)
    id_str, winning_str, actual_str = match.groups()
    winning = {int(n) for n in winning_str.split(' ') if n}
    actual = {int(n) for n in actual_str.split(' ') if n}
    combination = winning.intersection(actual)
    original_value = 0 if len(combination) == 0 else int(2**len(combination) - 1)
    return Card(
        id=int(id_str),
        winning=winning,
        actual=actual,
        original_value=original_value,
        combination=combination,
    )


cards = {card.id: card for line in input_ for card in [parse_card(line)]}

for card in cards.values():
    for copy_id in range(card.id + 1, card.id + 1 + len(card.combination)):
        card.copies.append(cards[copy_id])

instances_count = {card.id: 0 for card in cards.values()}

def update_instances_count(cards: list[Card]):
    for card in cards:
        instances_count[card.id] += 1
        update_instances_count(card.copies)


update_instances_count(list(cards.values()))
answer = sum(instances_count.values())
print(answer)

