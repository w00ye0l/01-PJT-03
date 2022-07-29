import sys

sys.stdin = open("_최빈수구하기.txt")


t = int(input())

for _ in range(1, t + 1):
    d = {}
    tt = int(input())
    arr = list(map(int, input().split()))               # 수들을 배열에 담는다

    for i in arr:                                       # d라는 딕셔너리에 수와 나온 횟수를 담는 반복문
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    # 딕셔너리를 값을 기준으로 내림차순, 키를 기준으로 내림차순 정렬한다
    d = sorted(d.items(), key=lambda x: (-x[1], -x[0]))

    # 정렬된 d는 리스트 안에 튜플 형태로 있기 때문에 가장 먼저 나오는(가장 빈도 수가 높은) 튜플의 0번째 수인 키를 출력한다
    print(f'#{tt} {d[0][0]}')
