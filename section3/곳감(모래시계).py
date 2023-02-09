# 현수는 곳감을 만들기 위해 감을 깍아 마당에 말리고 있습니다.
# 현수의 마당은 N*N 격자판으 로 이루어져 있으며, 현수는 각 격자 단위로 말리는 감의 수를 정합니다.
# 그런데 해의 위치에 따라 특정위치의 감은 잘 마르지 않습니다.
# 그래서 현수는 격자의 행을 기준으로 왼쪽, 또는 오른쪽으로 회전시켜 위치를 변경해 모든 감이 잘 마르게 합니다.
#
# 만약 회전명령 정보가 2 0 3이면 2번째 행을 왼쪽으로 3만큼 아래 그림처럼 회전시키는 명령 입니다.
#
# 첫 번째 수는 행번호, 두 번째 수는 방향인데 0이면 왼쪽, 1이면 오른쪽이고, 세 번째 수는 회전하는 격자의 수입니다.
# M개의 회전명령을 실행하고 난 후 아래와 같이 마당의 모래시계 모양의 영역에는 감이 총 몇 개가 있는지 출력하는 프로그램을 작성하세요.

# ▣ 입력설명
# 첫 줄에 자연수 N(3<=N<=20) 이 주어며, N은 홀수입니다.
# 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다.
# 이 자연수는 각 격자안에 있는 감의 개수이며, 각 격자안의 감의 개수는 100을 넘지 않는다.
# 그 다음 줄에 회전명령의 개수인 M(1<=M<=10)이 주어지고, 그 다음 줄부터 M개의 회전명령 정보가 M줄에 걸쳐 주어집니다.

# ▣ 출력설명
# 총 감의 개수를 출력합니다.


import sys

sys.stdin = open("곳감(모래시계).txt","rt")

N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
M = int(input())

#경준
# for i in range(M):
#     n, d, c = map(int,input().split())
#     #default:좌측이동
#     lst1 = lst[n-1][:c]  #빈자리 찾아가는 lst
#     lst2 = lst[n-1][c:N] #이동대상 lst
#     if d == 1:#우측이동
#         lst1 = lst[n-1][:N-c]
#         lst2 = lst[n-1][N-c:N]
#     lstIdx = 0
#
#     for j in range(N):
#         if len(lst2) > j:
#             lst[n-1][j] = lst2[j]
#         else:
#             lst[n-1][j] = lst1[lstIdx]
#             lstIdx += 1

#강의
for i in range(M):
    n, d, c = map(int,input().split())
    if d == 0:
        for _ in range(c):
            lst[n-1].append(lst[n-1].pop(0))
    else:
        for _ in range(c):
            lst[n-1].insert(0, lst[n-1].pop())

sum = 0
s, e = 0, N-1

for i in range(N):
    for j in range(s,e+1):
        sum += lst[i][j]
    if i < N//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(sum)
