def main():
    for i in range(1, 1000):
        for j in range(i+1, 1000):
            kSQ = (i*i) + (j*j)
            store = (i*i) + (j*j)
            if ((kSQ ** 0.5) ** 2) == store and i + j + (kSQ ** 0.5) == 1000:
                print(i * j * (kSQ ** 0.5))
                return


if __name__ == '__main__':
    main()