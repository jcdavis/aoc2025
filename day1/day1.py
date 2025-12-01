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
            position += num*dir
            position = ((position%100)+100)%100
            #print(f'After {line} at {position}')
            if position == 0:
                #print('Zero!')
                zeroes += 1
    print(zeroes)

if __name__ == "__main__":
    main()