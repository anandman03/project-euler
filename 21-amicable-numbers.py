import time


def amicable(n):
    ans = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ans.add(i)
            ans.add(int(n/i))
    return sum(ans) - n


def solve():
    ans = set()
    for i in range(1, 10001):
        a = amicable(i)
        b = amicable(a)
        if a != b and b == i:
            print(i, a)
            ans.add(i)
            ans.add(a)

    print(sum(ans))


def main():
    start = time.time()
    solve()
    print("Time: ", time.time() - start)


if __name__ == '__main__':
    main()
