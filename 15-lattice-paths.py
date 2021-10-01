import time


def solve():
    size = 20
    grid = [[0 for j in range(size+1)] for i in range(size+1)]

    grid[0][0] = 1
    for i in range(0, size+1):
        for j in range(0, size+1):
            grid[i][j] += grid[i-1][j] if i-1 >= 0 else 0
            grid[i][j] += grid[i][j-1] if j-1 >= 0 else 0
    print(grid[size][size])


def main():
    start = time.time()
    solve()
    print("Time: ", time.time() - start)


if __name__ == '__main__':
    main()
