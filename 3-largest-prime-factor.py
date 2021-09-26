def main():
    target = 600851475143
    limit = 10 ** 6 + 5

    sieve = [True for i in range(limit)]
    sieve[0] = sieve[1] = False
    for i in range(2, limit):
        if i * i > limit:
            break
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = False

    ans = 0
    for i in range(2, limit):
        if sieve[i] and target % i == 0:
            ans = i
    print(ans)


if __name__ == '__main__':
    main()
