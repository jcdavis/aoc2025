import argparse

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()
    max_area = 0
    points = []

    def is_legal(i: int, j: int):
        left = min(points[i][0], points[j][0])
        right = max(points[i][0], points[j][0])
        bottom = min(points[i][1], points[j][1])
        top = max(points[i][1], points[j][1])

        #Need to check corners actually, box could be interior

        e = i+1
        while e != i:
            (x, y) = points[e]
            (px, py) = points[e-1]
            if x == px:
                #Going up/down
                if x > left and x < right:
                    lb = min(y, py)
                    lt = max(y, py)
                    if (lb < top and lt > bottom) or (lb < top and lt > bottom):
                        return False
            else: # y == py
                #Going left/right
                if y > bottom and y < top:
                    ll = min(x, px)
                    lr = max(x, px)
                    if (ll < right and lr > left) or (ll < right and lr > right):
                        return False

            e = (e+1)%len(points)

        return True

    with open(args.file) as file:
        for line in file.readlines():
            [x, y] = line.split(',')
            points.append((int(x), int(y)))

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                if is_legal(i, j):
                    area = (abs(points[i][0]-points[j][0])+1)*(abs(points[i][1]-points[j][1])+1)
                    if area > max_area:
                        max_area = area

    print(max_area)

if __name__ == "__main__":
    main()