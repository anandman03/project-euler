import time


def multiply(arr, x):
    ans = []
    carry = 0
    for i in range(len(arr)-1, -1, -1):
        curr = (arr[i] * x) + carry
        ans.append(curr % 10)
        carry = curr // 10

    while carry:
        ans.append(carry % 10)
        carry //= 10

    ans.reverse()
    return ans


def solve():
    arr = [1]
    for i in range(2, 101):
        arr = multiply(arr, i)

    print(sum(arr))

def main():
    start = time.time()
    solve()
    print("Time: ", time.time() - start)


if __name__ == '__main__':
    main()
