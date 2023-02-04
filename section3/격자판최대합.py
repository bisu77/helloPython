# 5*5 격자판에 아래롸 같이 숫자가 적혀있습니다.
# N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가장 큰 합을 출력합니다.
#
# ▣ 입력설명
# 첫 줄에 자연수 N이 주어진다.(1<=N<=50)
# 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는다.
#
# ▣ 출력설명
# 최대합을 출력합니다.

import sys

sys.stdin = open("격자판최대합.txt","rt")

N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]

# 경준
# row = [0]*N
# col = [0]*N
# dia = [0]*2
#
# for idx, val in enumerate(lst):
#     for idx2, val2 in enumerate(val):
#         col[idx2] += val2
#         row[idx]  += val2
#         if idx == idx2:
#             dia[0] += val2
#         elif (idx+idx2) == N-1:
#             dia[1] += val2
#
# max = 0
# for i in row:
#     if max < i:
#         max = i
#
# for i in col:
#     if max < i:
#         max = i
#
# for i in dia:
#     if max < i:
#         max = i

# 강의
sum3 = 0
sum4 = 0
for i in range(N):
    sum1 = sum2 = 0
    for j in range(N):
        sum1 += lst[i][j]
        sum2 += lst[j][i]
        if i==j:
            sum3 += lst[i][j]
        elif (i+j) == (N-1):
            sum4 += lst[i][j]
max = sum1

if max < sum2:
    max = sum2
elif max < sum3:
    max = sum3
elif max < sum4:
    max = sum4

print(max)