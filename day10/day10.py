import argparse

def min_buttons(line: str) -> int:
    parts = line.split(' ')
    goal_str = parts[0][1:len(parts[0])-1]
    goal = 0
    for i in range(len(goal_str)):
        if goal_str[i] == '#':
            goal |= 1<<i
    buttons = []
    for button in parts[1:len(parts)-1]:
        parts = []
        for light in button[1:len(button)-1].split(','):
            parts.append(int(light))
        buttons.append(parts)

    cache = {}
    def recurse(status: int, state: int) -> int:
        if status == goal:
            return 0
        if state in cache:
            return cache[state]
        min_switch = 1000000
        for i in range(len(buttons)):
            if state & (1<<i) == 0:
                next_status = status
                for light in buttons[i]:
                    next_status ^= 1<<light
                min_switch = min(min_switch, 1+recurse(next_status, state | 1<<i))
        cache[state] = min_switch
        return min_switch

    return recurse(0, 0)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()

    sum = 0
    with open(args.file) as file:
        for line in file.readlines():
            sum += min_buttons(line)

    print(sum)

if __name__ == "__main__":
    main()