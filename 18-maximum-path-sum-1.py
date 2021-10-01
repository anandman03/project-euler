import time
from collections import deque


class container:
    def __init__(self, cost, x, y):
        self.cost, self.x, self.y = cost, x, y


def solve():
    nums = """
        75
        95 64
        17 47 82
        18 35 87 10
        20 04 82 47 65
        19 01 23 75 03 34
        88 02 77 73 07 63 67
        99 65 04 28 06 16 70 92
        41 41 26 56 83 40 80 70 33
        41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
        70 11 33 28 77 73 17 78 39 68 17 57
        91 71 52 38 17 14 91 43 58 50 27 29 48
        63 66 04 68 89 53 67 30 73 16 69 87 40 31
        04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    """

    arr = nums.split('\n')
    arr = [num.strip() for num in arr]
    arr = [num for num in arr if num != '']

    for i in range(len(arr)):
        arr[i] = arr[i].split(' ')
        arr[i] = [int(num.strip()) for num in arr[i]]

    MIN = -10**9
    dist = dict()
    dist["0-0"] = arr[0][0]

    queue = deque()
    queue.append(container(arr[0][0], 0, 0))

    ans = 0
    while len(queue) != 0:
        curr = queue.popleft()
        HASH = str(curr.x) + "-" + str(curr.y)

        if curr.x == len(arr)-1:
            ans = max(ans, curr.cost)
            continue

        if curr.x+1 < len(arr):
            HASH1 = str(curr.x+1) + "-" + str(curr.y)
            HASH2 = str(curr.x+1) + "-" + str(curr.y+1)

            if dist.get(HASH1, MIN) < dist.get(HASH) + curr.cost:
                dist[HASH1] = curr.cost + arr[curr.x+1][curr.y]
                queue.append(container(dist.get(HASH1), curr.x+1, curr.y))

            if curr.y+1 < len(arr[curr.x+1]) and dist.get(HASH2, MIN) < dist.get(HASH) + curr.cost:
                dist[HASH2] = curr.cost + arr[curr.x+1][curr.y+1]
                queue.append(container(dist.get(HASH2), curr.x+1, curr.y+1))
        else:
            continue

    print(ans)



def main():
    start = time.time()
    solve()
    print("Time: ", time.time() - start)


if __name__ == '__main__':
    main()
