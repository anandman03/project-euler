import time


def main():
    start = time.time()

    curr = 1
    inc = 2
    while True:
        count = 0
        for i in range(1, int(curr ** 0.5) + 1):
            if curr % i == 0:
                if curr // i == i:
                    count += 1
                else:
                    count += 2

        if count > 500:
            print(curr)
            break

        curr += inc
        inc += 1

    end = time.time()
    print(end - start)


if __name__ == '__main__':
    main()
