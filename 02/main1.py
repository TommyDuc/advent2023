import os
from dataclasses import dataclass

INPUT_FILE = "input"

with open(f"{os.path.dirname(__file__)}/{INPUT_FILE}", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]


@dataclass(frozen=True, slots=True)
class Draw:
    red: int = 0
    green: int = 0
    blue: int = 0

limit_draw = Draw(12, 13, 14)


@dataclass(frozen=True, slots=True)
class Game:
    id: int
    draws: list[Draw]


def parse_game(line: str) -> Game:
    g_str, d_str = line.split(':')
    _, id_str = g_str.split(' ')
    draws_str = d_str.split(';')

    draws: list[Draw] = []
    for draw_str in draws_str:
        pairs_str = draw_str.split(',')
        pairs: dict[str, int] = {}
        for pair_str in pairs_str:
            pair_str = pair_str.strip()
            count_str, color = pair_str.split(' ')
            pairs[color] = int(count_str)
        draws.append(Draw(**pairs))
    
    return Game(int(id_str), draws)
            

def is_game_possible(game: Game) -> bool:
    for draw in game.draws:
        if draw.red > limit_draw.red:
            return False
        if draw.green > limit_draw.green:
            return False
        if draw.blue > limit_draw.blue:
            return False
    return True


games = [parse_game(line) for line in input_]
possible_games = list(filter(lambda g: is_game_possible(g), games))
answer = sum(g.id for g in possible_games)
print(answer)
