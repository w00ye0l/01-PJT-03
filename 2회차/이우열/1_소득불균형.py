import sys

sys.stdin = open("_소득불균형.txt")

t = int(input())

for i in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    avg_ = sum(arr)/len(arr)
    cnt = 0

    for j in arr:
        if j <= avg_:
            cnt += 1

    print(f'#{i} {cnt}')
