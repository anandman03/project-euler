def main():
    limit = 2 * (10 ** 6)
    sieve = [True for i in range(limit)]

    for i in range(2, limit):
        if i*i > limit or not sieve[i]:
            continue
        for j in range(i*i, limit, i):
            sieve[j] = False

    ans = 0
    for i in range(2, limit):
        if sieve[i]:
            ans += i
    print(ans)


if __name__ == '__main__':
    main()