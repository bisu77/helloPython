# 지도 정보가 N*N 격자판에 주어집니다. 각 격자에는 그 지역의 높이가 쓰여있습니다.
# 각 격자판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역입니다.
# 봉우리 지역이 몇 개 있는 지 알아내는 프로그램을 작성하세요.
# 격자의 가장자리는 0으로 초기화 되었다고 가정한다.
#
# 만약 N=5 이고, 격자판의 숫자가 다음과 같다면 봉우리의 개수는 10개입니다.

# ▣ 입력설명
# 첫 줄에 자연수 N이 주어진다.(1<=N<=50)
# 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다.
# 각 자연수는 100을 넘지 않는다.
#
# ▣ 출력설명
# 봉우리의 개수를 출력하세요.

import sys

sys.stdin = open("봉우리.txt","rt")

N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(N):
        val = lst[i][j]
        dr = 0 #아래 row 값
        ur = 0 #위 row 값
        lc = 0 #왼쪽 col 값
        rc = 0 #오른쪽 col 값
        if i-1 >= 0:
            dr = lst[i-1][j]
        if i+1 < N:
            ur = lst[i+1][j]
        if j-1 >= 0:
            lc = lst[i][j-1]
        if j+1 < N:
            rc = lst[i][j+1]

        if val > dr and val > ur and val > lc and val > rc:
            cnt += 1

print(cnt)