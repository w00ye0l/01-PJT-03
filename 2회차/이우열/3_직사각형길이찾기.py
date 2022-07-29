import sys

sys.stdin = open("_직사각형길이찾기.txt")

t = int(input())

for i in range(1, t + 1):
    arr = list(map(int, input().split()))   # 직사각형 변의 길이 3개를 입력받는다
    d = {}                                  # 직사각형 변의 길이가 몇 번 입력됐는지 저장하는 딕셔너리를 만든다

    for j in arr:                           # 딕셔너리에 변의 길이가 이미 있으면 +1 없으면 1로 해주는 반복문
        if j not in d:
            d[j] = 1
        else:
            d[j] += 1

    for k, v in d.items():                  # 직사각형인 경우 덜 입력받은 변의 길이의 value가 1일 것이고
        if v == 1 or v == 3:                # 정사각형인 경우 value가 3일 것이다
            print(f'#{i} {k}')
