def main():
    limit = 4 * 10**6
    prev1, prev2 = 1, 2
    ans = 2

    while prev1 + prev2 <= limit:
        current = (prev1 + prev2)
        if current % 2 == 0:
            ans += current
        prev1 = prev2
        prev2 = current
    print(ans)


if __name__ == '__main__':
    main()
