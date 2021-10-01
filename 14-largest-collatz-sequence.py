import time


def main():
    start = time.time()

    cache = dict()
    maxLen, ans = 1, 1
    for num in range(2, 10 ** 6):
        curr = num
        count = 1
        while curr != 1:
            lookup = cache.get(curr, -1)
            if lookup != -1:
                count += lookup
                break
            if curr % 2 == 0:
                curr //= 2
            else:
                curr = 3*curr + 1
            count += 1

        cache[num] = count
        if count > maxLen:
            ans, maxLen = num, count

    print(ans)

    print("Time: ", time.time() - start)


if __name__ == '__main__':
    main()
