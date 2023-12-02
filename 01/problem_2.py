import os
import re


INPUT_FILE = "input"

with open(f"{os.path.dirname(__file__)}/{INPUT_FILE}", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]

associations = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}        

def convert_to_int(w: str) -> int:
    if w in associations.values():
        return int(w)
    return int(associations[w])


def get_line_numbers(line: str) -> int:
    numbers_expr = "|".join(f"({n})" for n in associations)
    re_expr = fr"(?=(\d)|{numbers_expr})"
    matches = re.findall(re_expr, line)
    numbers = [convert_to_int(n) for groups in matches for n in groups if n]
    number_str = f"{numbers[0]}{numbers[-1]}"
    number = int(number_str)
    print(f"{line} -> {number}")
    return number


s = sum(
    get_line_numbers(line)
    for line in input_
)
print(s)
