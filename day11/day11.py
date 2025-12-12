import argparse

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()
    adj = {}
    cache = {}

    def recurse(current: str, goal: str) -> int:
            if current == goal:
                 return 1
            if current in cache:
                 return cache[current]
            sum = 0
            for neighbor in adj.get(current, []):
                sum += recurse(neighbor, goal)
            cache[current] = sum
            return sum

    with open(args.file) as file:
        for line in file.readlines():
            parts = line.strip().split(' ')
            adj[parts[0][0:len(parts[0])-1]] = parts[1:]

        total = recurse('svr', 'fft')
        cache = {}
        total *= recurse('fft', 'dac')
        cache = {}
        total *= recurse('dac', 'out')
        print(total)

if __name__ == "__main__":
    main()