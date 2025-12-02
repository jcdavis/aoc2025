import argparse

def is_valid(num: int) -> bool:
    as_str = str(num)
    for pattern_len in range(1, (len(as_str)//2)+1):
        if len(as_str) % pattern_len != 0:
            continue
        pattern = as_str[:pattern_len]
        if as_str == "".join([pattern]*(len(as_str)//pattern_len)):
            return False
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()
    sum = 0
    with open(args.file) as file:
        for part in file.readline().split(','):
            bounds = part.split('-')
            left = int(bounds[0])
            right = int(bounds[1])
            for i in range(left, right+1):
                if not is_valid(i):
                    sum += i
    print(sum)

if __name__ == "__main__":
    main()