def main():
    ans = 0
    for i in range(100, 1000):
        for j in range(i+1, 1000):
            product = str(i * j)
            reverse = product[::-1]
            if product == reverse:
                ans = max(ans, int(product))
    print(ans)


if __name__ == '__main__':
    main()
