import sys

sys.stdin = open("_직사각형길이찾기.txt")

t = int(input())

for i in range(1, t + 1):
    arr = list(map(int, input().split()))
    d = {}

    for j in arr:
        if j not in d:
            d[j] = 1
        else:
            d[j] += 1

    for k, v in d.items():
        if v == 1 or v == 3:
            print(f'#{i} {k}')
