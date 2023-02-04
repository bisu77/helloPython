# N개의 수로 된 수열 A[1], A[2], ..., A[N] 이 있다.
# 이 수열의 i번째 수부터 j번째 수까지의 합 A[i]+A[i+1]+...+A[j-1]+A[j]가
# M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

# ▣ 입력설명
# 첫째 줄에 N(1≤N≤10,000), M(1≤M≤300,000,000)이 주어진다.
# 다음 줄에는 A[1], A[2], ..., A[N]이 공백으로 분리되어 주어진다.
# 각각의 A[x]는 30,000을 넘지 않는 자연수이다.
#
# ▣ 출력설명
# 첫째 줄에 경우의 수를 출력한다.

import sys
sys.stdin = open("수들의합.txt","rt")

N,M = map(int, input().split())
lst = list(map(int,input().split()))

cnt = 0
sum = 0
# 경준
# for val in lst:
#     if val > M:
#         sum = 0
#         continue
#     elif val == M:
#         cnt += 1
#         sum = 0
#         continue
#     elif val < M:
#         sum += val
#         if sum == M:
#             cnt += 1
#             sum = val
#         elif sum > M:
#             sum = 0
#             continue

# 강의
lt = 0
rt = 1
tot = lst[0]
cnt = 0

while True:
    if tot < M:
        if rt < N:
            tot += lst[rt]
            rt += 1
        else:
            break
    elif tot == M:
        tot -= lst[lt]
        lt += 1
        cnt += 1
    else:
        tot -= lst[lt]
        lt += 1
print(cnt)