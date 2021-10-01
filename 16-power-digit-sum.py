import time


def solve():
    ans = 0
    num = str(2 ** 1000)
    for c in num:
        ans += int(c)
    print(ans)


def main():
    start = time.time()
    solve()
    print("Time: ", time.time() - start)


if __name__ == '__main__':
    main()
