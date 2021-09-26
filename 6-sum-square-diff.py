def main():
    ans1, ans2 = 0, 0
    for i in range(1, 101):
        ans1 += (i ** 2)
        ans2 += i

    print((ans2 ** 2) - ans1)


if __name__ == '__main__':
    main()