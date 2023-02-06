# 현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자 안에는 한 그루의 사과나무가 심어저 있다.
# N의 크기는 항상 홀수이다.
# 가을이 되어 사과를 수확해야 하는데 현수는 격자판 안의 사과를 수확할 때 다이아몬드 모양의 격자판만 수확하고
# 나머지 격자안의 사과는 새들을 위해서 남겨놓는다.
#
# 만약 N이 5이면 아래 그림과 같이 진한 부분의 사과를 수확한다.
#
# 현수과 수확하는 사과의 총 개수를 출력하세요.


# ▣ 입력설명
# 첫 줄에 자연수 N(홀수)이 주어진다.(3<=N<=20)
# 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다.
# 이 자연수는 각 격자안에 있는 사과나무에 열린 사과의 개수이다.
#
# 각 격자안의 사과의 개수는 100을 넘지 않는다.

# ▣ 출력설명
# 수확한 사과의 총 개수를 출력합니다.

import sys

sys.stdin = open("사과나무(다이아몬드).txt","rt")

N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
# 경준
# center = N // 2
# colA = 0
# colB = 0
# sum = 0
#
# for rowIdx, rowVal in enumerate(lst):
#     if rowIdx == 0 or rowIdx == N-1:
#         colA = N // 2
#         colB = N // 2
#     elif rowIdx <= center:
#         colA -= 1
#         colB += 1
#     else:
#         colA += 1
#         colB -= 1
#     for colIdx, colVal in enumerate(rowVal):
#         if colA <= colIdx <= colB:
#             sum += colVal

# 강의
s = e = N // 2
sum = 0

for i in range(N):
    for j in range(s, e+1):
        sum += lst[i][j]
    if i < N//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(sum)
