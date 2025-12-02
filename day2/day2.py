import argparse

def is_valid(num: int) -> bool:
    as_str = str(num)
    if len(as_str) % 2 == 1:
        return True
    half = len(as_str) // 2
    return as_str[:half] != as_str[half:]

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
                    #print(i)
                    sum += i
    print(sum)

if __name__ == "__main__":
    main()