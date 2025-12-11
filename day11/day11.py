import argparse

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()
    adj = {}

    def recurse(current: str, visited: set[str]) -> int:
        if current == 'out':
            return 1
        if current in visited:
            return 0
        visited.add(current)
        counts = 0
        for neighbor in adj.get(current, []):
            counts += recurse(neighbor, visited)
        visited.remove(current)
        return counts

    with open(args.file) as file:
        for line in file.readlines():
            parts = line.strip().split(' ')
            adj[parts[0][0:len(parts[0])-1]] = parts[1:]

        print(recurse('svr', set()))

if __name__ == "__main__":
    main()