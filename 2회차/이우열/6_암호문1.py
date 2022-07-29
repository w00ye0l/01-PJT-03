import sys

sys.stdin = open("_암호문1.txt")


for t in range(1, 11):
    n = int(input())                            # 원본 암호문의 길이
    arr = list(input().split())                 # 원본 암호문

    o_n = int(input())                          # 명령어 개수
    order = list(input().split())               # 명령어

    idx = 0                                     # 삽입해야 하는 암호문이 들어갈 원본 암호문의 인덱스
    i_count = 0                                 # 삽입해야 하는 암호문의 개수

    for i in range(len(order)):

        if order[i] == 'I':                     # 명령어가 'I'일 때
            idx = int(order[i + 1])             # 명령어가 들어갈 위치를 idx에 저장
            i_count = int(order[i + 2])         # 삽입할 암호문의 개수를 i_count에 저장

            for j in range(i_count-1, -1, -1):  # i_count를 역순으로 반복하면서 삽입할 암호문을 뒤에서부터 저장
                # 명령어의 'I' 이후 세 인덱스를 건너뛰어 삽입할 암호문의 숫자를 원본 암호문에 끼워넣는다
                arr.insert(idx, order[i + 3 + j])

    # 수정된 원본 암호문의 10개의 수를 잘라서 공백을 포함하여 하나의 문자열로 변환
    result = ' '.join(arr[:10])

    print(f'#{t} {result}')
