import argparse

def can_access(grid: list[str], i: int, j: int) -> bool:
    adj = 0

    for di in range(-1, 2):
        for dj in range(-1, 2):
            if di != 0 or dj != 0:
                ni = i + di
                nj = j + dj
                if ni >= 0 and ni < len(grid) and nj >= 0 and nj < len(grid[ni]):
                    if grid[ni][nj] == '@':
                        adj += 1
    return adj < 4

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()
    sum = 0
    with open(args.file) as file:
        grid = file.readlines()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '@' and can_access(grid, i, j):
                    sum += 1

    print(sum)

if __name__ == "__main__":
    main()