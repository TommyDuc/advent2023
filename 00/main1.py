import os


INPUT_FILE = "input_test"

with open(f"{os.path.dirname(__file__)}/{INPUT_FILE}", mode='r') as file:
    input_ = [line.strip() for line in file.readlines() if line]


for line in input_:
    print(line)
