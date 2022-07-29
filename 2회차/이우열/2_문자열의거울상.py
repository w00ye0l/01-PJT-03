import sys

sys.stdin = open("_문자열의거울상.txt")

t = int(input())

for i in range(1, t + 1):
    s = input()                 # 문자열을 입력받는다
    r_s = list(s[::-1])         # 입력받은 문자열을 뒤집어 리스트에 저장한다
    result = []

    for j in r_s:               # 뒤집은 문자열 리스트를 하나씩 보면서 거울 형식에 맞게 변환해준다
        if j == 'p':            # 더 간단한 방법이 있을 것 같다
            result.append('q')
        elif j == 'q':
            result.append('p')
        elif j == 'b':
            result.append('d')
        elif j == 'd':
            result.append('b')
    result = ''.join(result)    # 리스트를 공백이 없는 문자열로 바꾸어준다

    print(f'#{i} {result}')
