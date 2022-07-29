import sys

sys.stdin = open("_소득불균형.txt")

t = int(input())

for i in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    avg_ = sum(arr) / len(arr)              # 소득의 합을 길이로 나누어 평균을 구한다
    cnt = 0

    for j in arr:                           # 소득이 평균 이하인 경우 cnt를 하나씩 늘린다
        if j <= avg_:
            cnt += 1

    print(f'#{i} {cnt}')
