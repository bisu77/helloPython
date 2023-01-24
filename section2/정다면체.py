# 두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중
# 가장 확률이 높은 숫자를 출력하는 프로그램을 작성하세요.
#
# 정답이 여러 개일 경우 오름차순으로 출력합니다.
#
# ▣ 입력설명
# 첫 번째 줄에는 자연수 N과 M이 주어집니다. N과 M은 4, 6, 8, 12, 20 중의 하나입니다.

# ▣ 출력설명
# 첫 번째 줄에 답을 출력합니다.
#
# ▣ 입력예제
# 4 6
#
# ▣ 출력예제
# 5 6 7

import sys

sys.stdin = open("정다면체.txt", "rt")

N, M = map(int, input().split())
l = [0]*(N+M+1)

for i in range(1,N+1):
    for ii in range(1,M+1):
        l[i+ii]+=1

max = -216000000

for i in range(N+M+1):
    if l[i]>max:
        max = l[i]

for i in range(N+M+1):
    if l[i]==max:
        print(i,end=' ')