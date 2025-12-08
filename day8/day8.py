import argparse
import heapq

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()
    parents = {}
    sizes = {}

    def find(a: int) -> int:
        root = a
        while parents[root] != root:
            root = parents[root]
        parents[a] = root
        return root

    def union(a: int, b: int) -> bool:
        a = find(a)
        b = find(b)
        if a == b:
            return False

        if sizes[a] > sizes[b]:
            parents[b] = a
            sizes[a] += sizes[b]
            del sizes[b]
        else:
            parents[a] = b
            sizes[b] += sizes[a]
            del sizes[a]
        return True

    with open(args.file) as file:
        points = []
        for line in file.readlines():
            [x, y, z] = line.split(',')
            points.append((int(x), int(y), int(z)))
        heap = []
        for i in range(len(points)):
            parents[i] = i
            sizes[i] = 1
            for j in range(i+1, len(points)):
                    dist = (
                        abs(points[i][0]-points[j][0])**2 +
                        abs(points[i][1]-points[j][1])**2 +
                        abs(points[i][2]-points[j][2])**2
                    )
                    heapq.heappush(heap, (dist, i, j))

        while True:
            (dist, i, j) = heapq.heappop(heap)
            union(i, j)
            if len(sizes) == 1:
                print(points[i][0]*points[j][0])
                break



if __name__ == "__main__":
    main()