# 유럽에서 가장 유명했던 유람선 타이타닉이 침몰하고 있습니다. 유람선에는 N명의 승객이 타고 있습니다.
# 구명보트를 타고 탈출해야 하는데 타이타닉에 있는 구명보트는 2명 이하로만 탈 수 있으며,
# 보트 한 개에 탈 수 있는 총 무게도 M kg 이하로 제한되어 있습니다.
#
# N명의 승객 몸무게가 주어졌을 때 승객 모두가 탈출하기 위한 구명보트의 최소개수를 출력하는 프로그램을 작성하세요.

# ▣ 입력설명
# 첫째 줄에 자연수 N(5<=N<=1000)과 M(70<=M<=250)이 주어집니다.
# 두 번째 줄에 N개로 구성된 몸무게 수열이 주어집니다. 몸무게는 50이상 150이하입니다.
# 각 승객의 몸무게는 M을 넘지는 않습니다. 즉 탈출을 못하는 경우는 없습니다.
#
# ▣ 출력설명
# 첫째 줄에 구명보트의 최소 개수를 출력합니다.

import sys

sys.stdin = open("침몰하는타이타닉.txt","rt")

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst2 = [0]*N

lst.sort()
idx = 0
cnt = 0

for i in range(N):
    maxWeight = 0

    if lst2[i] == 0:
        for ii in range(i+1, N):
            if lst2[ii] == 0:
                weight = lst[i] + lst[ii]
                if weight == M:
                    lst2[i] += 1
                    lst2[ii] += 1
                    cnt += 1
                    break
                if weight < M and maxWeight < weight:
                    maxWeight = weight
                    idx = ii
        else:
            lst2[i] += 1
            lst2[idx] += 1
            cnt += 1

print(cnt)