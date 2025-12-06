import argparse
from collections import defaultdict

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()
    sum = 0
    cols = defaultdict(list)
    with open(args.file) as file:
        for line in file.readlines():
            parts = line.split()
            for i in range(0, len(parts)):
                cols[i].append(parts[i])

        for col in cols:
            op = cols[col].pop()
            acc = 1 if op == '*' else 0
            for elem in cols[col]:
                if op == '*':
                    acc *= int(elem)
                else:
                    acc += int(elem)
            sum += acc



    print(sum)

if __name__ == "__main__":
    main()