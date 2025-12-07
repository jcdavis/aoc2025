import argparse

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()
    sum = 0
    with open(args.file) as file:
        data = file.readlines()
        beams = set([data[0].find('S')])
        i = 1
        for i in range(1, len(data)):
            for j in range(len(data[i])):
                if data[i][j] == '^':
                    if j in beams:
                        beams.remove(j)
                        beams.add(j-1)
                        beams.add(j+1)
                        sum += 1

    print(sum)

if __name__ == "__main__":
    main()