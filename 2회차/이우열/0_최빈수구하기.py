import sys

sys.stdin = open("_최빈수구하기.txt")


t = int(input())

for _ in range(1, t + 1):
    d = {}
    tt = int(input())
    arr = list(map(int, input().split()))

    for i in arr:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    d = sorted(d.items(), key=lambda x: x[1], reverse=True)

    print(f'#{tt} {d[0][0]}')
