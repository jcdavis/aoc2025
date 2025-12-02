import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()
    position = 50
    zeroes = 0
    print("Running")
    with open(args.file) as file:
        for line in file.readlines():
            num = int(line[1:])
            dir = -1 if line[0] == 'L' else 1
            zeroes += num // 100
            num %= 100
            position += num*dir
            if position == 0:
                zeroes += 1
            elif position > 0:
                if position >= 100:
                    zeroes += 1
                    position -= 100
            else:
                if dir*num == position:
                    zeroes -= 1
                if position < 0:
                    zeroes += 1
                    position += 100

    print(zeroes)

if __name__ == "__main__":
    main()