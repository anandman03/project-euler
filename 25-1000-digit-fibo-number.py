import time


def solve():
    a, b, c, index = 1, 1, 0, 2
    while len(str(c)) != 1000:
        index += 1
        c = a + b
        a = b
        b = c

    print(index)


def main():
    start = time.time()
    solve()
    print(time.time() - start)


if __name__ == '__main__':
    main()
