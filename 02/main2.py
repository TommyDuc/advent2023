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
            

def minimal_draw(draws: list[Draw]) -> Draw:
    red, green, blue = [0] * 3
    for draw in draws:
        red = max(red, draw.red)
        green = max(green, draw.green)
        blue = max(blue, draw.blue)
    return Draw(red, green, blue)


def draw_power(draw: Draw) -> int:
    return draw.red * draw.green * draw.blue


games = [parse_game(line) for line in input_]
min_draws = [minimal_draw(g.draws) for g in games]
answer = sum(draw_power(d) for d in min_draws)
print(answer)
