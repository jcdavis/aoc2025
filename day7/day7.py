import argparse

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()

    with open(args.file) as file:
        data = file.readlines()
        start = data[0].find('S')
        cache = {}

        def recurse(row: int, col: int) -> int:
            if col < 0 or col > len(data[0]):
                return 0
            if row == len(data):
                return 1
            if (row, col) in cache:
                return cache[(row, col)]
            result = -1
            if data[row][col] == '^':
                result = recurse(row+1, col-1) + recurse(row+1, col+1)
            else:
                result = recurse(row+1, col)
            cache[(row, col)] = result
            return result

        print(recurse(1, start))

if __name__ == "__main__":
    main()