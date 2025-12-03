import argparse

def joltage(bank: str) -> int:
    ints = [int(c) for c in bank]
    cache = {}
    def recurse(i: int, digits: int) -> int:
        if digits == 0:
            return 0
        if i == len(ints):
            return float("-inf")
        if (i, digits) in cache:
            return cache[(i, digits)]
        take = ints[i] * (10**(digits-1)) + recurse(i+1, digits-1)
        skip = recurse(i+1, digits)
        cache[(i, digits)] = max(take, skip)
        return max(take, skip)
    result = recurse(0, 12)
    return result


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