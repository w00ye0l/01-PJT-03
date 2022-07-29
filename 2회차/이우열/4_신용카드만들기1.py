import sys

sys.stdin = open("_신용카드만들기1.txt")

t = int(input())

for i in range(1, t + 1):
    arr = list(map(int, input().split()))
    sum_ = 0

    for j in range(len(arr)):
        if (j + 1) % 2 == 1:
            sum_ += arr[j] * 2
        else:
            sum_ += arr[j]

    if sum_ % 10 == 0:
        result = 0
    else:
        result = 10 - (sum_ % 10)

    print(f'#{i} {result}')
