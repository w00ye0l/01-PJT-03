import sys

sys.stdin = open("_신용카드만들기2.txt")

t = int(input())
check = ['3', '4', '5', '6', '9']

for i in range(1, t + 1):
    arr = list(input())

    if arr[0] not in check:
        print(f'#{i} 0')
    elif len(arr) - arr.count('-') != 16:
        print(f'#{i} 0')
    else:
        print(f'#{i} 1')
