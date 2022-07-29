import sys

sys.stdin = open("_신용카드만들기1.txt")

t = int(input())

for i in range(1, t + 1):
    arr = list(map(int, input().split()))   # 입력받은 신용카드 번호의 공백을 지워 리스트로 만든다
    sum_ = 0

    for j in range(len(arr)):               # 입력받은 번호의 길이만큼 반복문
        if (j + 1) % 2 == 1:                # 인덱스는 0부터 시작하기 때문에 1을 더해주어 몇 번째 자리수인지 판단 후 홀수일 때
            sum_ += arr[j] * 2              # 2를 곱하여 sum_에 누적
        else:                               # 짝수일 때
            sum_ += arr[j]                  # 그냥 누적

    if sum_ % 10 == 0:                      # 마지막 자리 N을 제외한 sum_이 10으로 나누어 떨어지면 N은 0
        result = 0
    else:                                   # 10으로 나누어 떨어지지 않으면 10을 채우기 위해 나머지를 구해 10에서 빼준다
        # ex) 51 => 51 % 10 = 1 => 10 - 1 = 9 = N
        result = 10 - (sum_ % 10)

    print(f'#{i} {result}')
