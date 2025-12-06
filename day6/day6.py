import argparse
from typing import Optional

def parse_number(data: list[str], col: int) -> Optional[int]:
    i = 0
    sum = 0
    while i < len(data)-1 and data[i][col] == ' ':
        i += 1
    if i == len(data)-1:
        return None
    while i < len(data)-1 and data[i][col] != ' ':
        sum *= 10
        sum += int(data[i][col])
        i += 1
    return sum

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()
    sum = 0
    with open(args.file) as file:
        data = file.readlines()
        j = 0
        op = '+'
        acc = 0
        while j < len(data[0])-1:
            if data[-1][j] != ' ':
                sum += acc
                op = data[-1][j]
                acc = 0 if op == '+' else 1
            num = parse_number(data, j)
            if num is not None:
                if op == '+':
                    acc += num
                else:
                    acc *= num
            j += 1

        sum += acc

    print(sum)

if __name__ == "__main__":
    main()