import sys

sys.stdin = open("_암호문1.txt")


for t in range(1, 11):
    n = int(input())
    arr = list(input().split())

    o_n = int(input())
    order = list(input().split())

    idx = 0
    start_point = 0

    for i in range(len(order)):
        ss = []

        if order[i] == 'I':
            idx = int(order[i+1])
            start_point = int(order[i+2])

            for j in range(start_point-1, -1, -1):
                arr.insert(idx, order[i + 3 + j])

    result = ' '.join(arr[:10])

    print(f'#{t} {result}')
