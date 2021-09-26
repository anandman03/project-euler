def main():
    size = 10**6 + 51
    limit = 10**4

    sieve = [True for i in range(size)]
    for i in range(2, size):
        if i*i > size or not sieve[i]:
            continue
        for j in range(i*i, size, i):
            sieve[j] = False

    primes = []
    for i in range(2, size):
        if sieve[i]:
            primes.append(i)

    print(primes[limit])


if __name__ == '__main__':
    main()
