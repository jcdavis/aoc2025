import argparse

def joltage(bank: str) -> int:
    max_first = int(bank[0])
    max_second = 0
    for c in bank[1:len(bank)-1]:
        val = int(c)
        if val > max_first:
            max_first = val
            max_second = 0
        elif val > max_second:
            max_second = val
    max_second = max(max_second, int(bank[-1]))
    return max_first*10 + max_second


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()
    sum = 0
    with open(args.file) as file:
        for line in file.readlines():
            sum += joltage(line.strip())

    print(sum)

if __name__ == "__main__":
    main()