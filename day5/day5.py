import argparse

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()
    sum = 0
    ranges = []
    with open(args.file) as file:
        lines = file.readlines()
        i = 0
        while len(lines[i]) > 1:
            parts = lines[i].split('-')
            ranges.append((int(parts[0]), int(parts[1])))
            i += 1
        ranges.sort(key=lambda x: x[0])
        j = 1
        merged = []
        start = ranges[0][0]
        end = ranges[0][1]
        while j < len(ranges):
            if end < ranges[j][0]:
                # push squashed
                merged.append((start, end))
                start = ranges[j][0]
                end = ranges[j][1]
            else:
                # extend:
                end = max(end, ranges[j][1])
            j += 1
        merged.append((start, end))
        for (start, end) in merged:
            sum += end - start + 1


    print(sum)

if __name__ == "__main__":
    main()