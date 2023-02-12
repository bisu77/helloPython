# 1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면 격자판 위에서 가로방향 또는 세로방향으로
# 길이 5자리 회문수가 몇 개 있는지 구하는 프로그램을 작성하세요.
#
# 회문수란 121과 같이 앞에서부터 읽으나 뒤에서부터 읽으나 같은 수를 말합니다.
# 빨간색처럼 구부러진 경우(87178)는 회문수로 간주하지 않습니다.
#
# ▣ 입력설명
# 1부터 9까지의 자연수로 채워진 7*7격자판이 주어집니다.
#
# ▣ 출력설명
# 5자리 회문수의 개수를 출력합니다.

import sys

sys.stdin = open("격자판회문수.txt","rt")

lst = [list(map(int,input().split())) for _ in range(7)]

# 내 방식
# rowCnt = 0
# colCnt = 0
# e = 4
# sum = 0
# for i in range(7):
#     for j in range(3):
#         rowCnt = 0
#         colCnt = 0
#         e = 4
#         for k in range(2):
#             if lst[i][j+k] == lst[i][j+e]:
#                 rowCnt += 1
#             if lst[j+k][i] == lst[j+e][i]:
#                 colCnt += 1
#             e -= 1
#         if rowCnt == 2:
#             sum += 1
#         if colCnt == 2:
#             sum += 1

# 강의
sum = 0
for i in range(3):
    for j in range(7):
        tmp = lst[j][i:i+5]
        if tmp == tmp[::-1]: #row check
            sum += 1

        for k in range(2):#col check
            if lst[i+k][j] != lst[i+4-k][j]:
                break
        else:
            sum += 1

print(sum)