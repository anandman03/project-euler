import time


def cycleLength(d):
    HashMap = dict()

    itr, mod = 0, 1
    while True:
        mod = (10 * mod) % d
        if HashMap.get(mod, -1) != -1:
            return itr - HashMap.get(mod)
        HashMap[mod] = itr
        itr += 1

    return -1


def solve():
    ans, maxCycle = 0, 0
    for d in range(1, 1000):
        curr = cycleLength(d)
        if curr > maxCycle:
            ans, maxCycle = d, curr

    print(ans)


def main():
    start = time.time()
    solve()
    print(time.time() - start)


if __name__ == '__main__':
    main()
