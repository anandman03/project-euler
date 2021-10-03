import time


def div(n):
    factors = set([1])
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return sum(factors)


def solve():
    limit = 28124

    abundant = set(i for i in range(1, limit) if div(i) > i)
    sumAbundant = set(x + y for x in abundant for y in abundant)
    allNums = set(range(1, limit))
    print(sum(allNums - sumAbundant))


def main():
    start = time.time()
    solve()
    print(time.time() - start)


if __name__ == "__main__":
    main()
