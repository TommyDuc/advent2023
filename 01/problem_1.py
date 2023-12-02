import os
import re


INPUT_FILE = "input"

with open(f"{os.path.dirname(__file__)}/{INPUT_FILE}", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]


def get_line_numbers(line: str) -> int:
    matches = re.finditer(r"(\d)", line)
    numbers_str = [m.group(1) for m in matches]
    number_str = f"{numbers_str[0]}{numbers_str[-1]}"
    number = int(number_str)
    print(f"{line} -> {number}")
    return number
    


s = sum(
    get_line_numbers(line)
    for line in input_
)
print(s)
