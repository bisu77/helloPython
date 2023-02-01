# 오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로그램을 작성하세요.
#
# ▣ 입력설명
# 첫 번째 줄에 첫 번째 리스트의 크기 N(1<=N<=100)이 주어집니다. 두 번째 줄에 N개의 리스트 원소가 오름차순으로 주어집니다.
# 세 번째 줄에 두 번째 리스트의 크기 M(1<=M<=100)이 주어집니다. 네 번째 줄에 M개의 리스트 원소가 오름차순으로 주어집니다.
# 각 리스트의 원소는 int형 변수의 크기를 넘지 않습니다.
#
# ▣ 출력설명
# 오름차순으로 정렬된 리스트를 출력합니다.

import sys

sys.stdin = open("리스트2개합치기.txt","rt")

N = int(input())
lst1 = list(map(int, input().split()))
M = int(input())
lst2 = list(map(int, input().split()))

lst3 = list()

loopCnt = N+M

p1 = 0
p2 = 0

# for i in range(loopCnt):
#     if p1 == N:
#         lst3.append(lst2[p2])
#         p2 += 1
#     elif p2 == M:
#         lst3.append(lst1[p1])
#         p1 += 1
#     elif lst1[p1] < lst2[p2]:
#         lst3.append(lst1[p1])
#         p1 += 1
#     else:
#         lst3.append(lst2[p2])
#         p2 += 1

while p1<N and p2<M:
    if lst1[p1]<=lst2[p2]:
        lst3.append(lst1[p1])
        p1+=1
    else:
        lst3.append(lst2[p2])
        p2+=1

if p1==N:
    lst3 = lst3+lst2[p1:]
elif p2==M:
    lst3 = lst3+lst1[p2:]

for i in lst3:
    print(i, end=' ')