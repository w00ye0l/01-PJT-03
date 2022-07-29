import sys

sys.stdin = open("_신용카드만들기2.txt")

t = int(input())
check = ['3', '4', '5', '6', '9']           # 신용 카드 번호에서 첫 번째로 시작해야 하는 숫자들

for i in range(1, t + 1):
    arr = list(input())

    if arr[0] not in check:                 # 카드 번호의 첫 번째 숫자가 시작해야 하는 숫자들이 아닐 경우
        print(f'#{i} 0')                    # 0 출력
    elif len(arr) - arr.count('-') != 16:   # 카드 번호의 길이가 16이 아닐 경우('-'이 있을 경우 '-'의 개수를 빼준다)
        print(f'#{i} 0')                    # 0 출력
    else:                                   # 나머지는 다 참이므로 1 출력
        print(f'#{i} 1')
