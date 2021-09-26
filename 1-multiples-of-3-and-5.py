def main():
    ans = 0
    for num in range(0, 1000):
        if num % 3 == 0 or num % 5 == 0:
            ans += num
    print(ans)


if __name__ == '__main__':
    main()
