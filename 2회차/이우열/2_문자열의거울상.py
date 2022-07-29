import sys

sys.stdin = open("_문자열의거울상.txt")

t = int(input())

for i in range(1, t + 1):
    s = input()
    r_s = list(s[::-1])
    result = []

    for j in r_s:
        if j == 'p':
            result.append('q')
        elif j == 'q':
            result.append('p')
        elif j == 'b':
            result.append('d')
        elif j == 'd':
            result.append('b')
    result = ''.join(result)

    print(f'#{i} {result}')
