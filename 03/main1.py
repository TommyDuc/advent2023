from collections.abc import Generator
import os
import re
from dataclasses import dataclass


INPUT_FILE = "input"

with open(f"{os.path.dirname(__file__)}/{INPUT_FILE}", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]
I_MAX = len(input_) - 1
J_MAX = len(input_[0]) - 1


@dataclass(frozen=True, slots=True)
class Symbol:
    symbol: str
    i: int
    j: int


@dataclass(frozen=True, slots=True)
class Number:
    j_start: int
    j_end: int
    i: int
    value: int
    symbols: list[Symbol]


def get_line_numbers(line: str, j: int) -> list[Number]:
    matches = re.finditer(r"(\d+)", line)
    numbers: list[Number] = []
    for match in matches:
        if match is None:
            continue
        numbers.append(number_from_match(match, j))
    return numbers


def number_from_match(match: re.Match[str], i: int) -> Number:
    start = match.start()
    end = match.end() - 1

    symbols: list[Symbol] = []
    for i_, j_ in pos_around_iterator(i, start, end):
        c = input_[i_][j_]
        if c not in '.0123456789':
            symbols.append(Symbol(c, i_, j_))

    return Number(start, end, i, int(match.group(0)), symbols)


def pos_around_iterator(i: int, j_start: int, j_end: int) -> Generator[tuple[int, int], None]:
    # left line
    if j_start > 0:
        if i > 0:
            yield i - 1, j_start - 1
        yield i, j_start - 1
        if i < I_MAX:
            yield i + 1, j_start - 1
    
    # right line
    if j_end < J_MAX:
        if i > 0:
            yield i - 1, j_end + 1
        yield i, j_end + 1
        if i < I_MAX:
            yield i + 1, j_end + 1

    # top line
    if i > 0:
        for j in range(j_start, j_end + 1):
            yield i - 1, j

    # bottom line
    if i < I_MAX:
        for j in range(j_start, j_end + 1):
            yield i + 1, j



numbers: list[Number] = []
for line_number, line in enumerate(input_):
    numbers.extend(get_line_numbers(line, line_number))

numbers_with_symbols = list(filter(lambda n: len(n.symbols) > 0, numbers))
answer = sum(n.value for n in numbers_with_symbols)
print(answer)
