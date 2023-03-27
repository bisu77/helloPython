# 1부터 N까지의 모든 자연수로 구성된 길이 N의 수열이 주어집니다.
# 이 수열의 왼쪽 맨 끝 숫자 또는 오른쪽 맨 끝 숫자 중 하나를 가져와 나열하여 가장 긴 증가수열을 만듭니다.
#
# 이 때 수열에서 가져온 숫자(왼쪽 맨 끝 또는 오른쪽 맨 끝)는 그 수열에서 제거됩니다.
# 예를 들어 2 4 5 1 3 이 주어지면 만들 수 있는 가장 긴 증가수열의 길이는 4입니다.
#
# 맨 처음 왼쪽 끝에서 2를 가져오고, 그 다음 오른쪽 끝에서 3을 가져오고, 왼쪽 끝에서 4,
# 왼쪽 끝에서 5를 가져와 2 3 4 5 증가수열을 만들 수 있습니다.

# ▣ 입력설명
# 첫째 줄에 자연수 N(3<=N<=100)이 주어집니다.
# 두 번째 줄에 N개로 구성된 수열이 주어집니다.

# ▣ 출력설명
# 첫째 줄에 최대 증가수열의 길이를 출력합니다.
# 두 번째 줄에 가져간 순서대로 왼쪽 끝에서 가져갔으면 'L', 오른쪽 끝에서 가져갔으면 'R'를 써 간 문자열을 출력합니다.
# (단 마지막에 남은 값은 왼쪽 끝으로 생각합니다.)

import sys
from collections import deque

sys.stdin = open("증가수열만들기.txt","rt")

N = int(input())
lst = list(map(int, input().split()))
# lst = deque(lst)
#
# str = ''
# lastNum = 0
#
# while lst:
#     first = lst[0]
#     last = lst[len(lst)-1]
#     fAbs = abs(lastNum - first)
#     lAbs = abs(lastNum - last)
#
#     if lastNum < first and lAbs > fAbs:
#         str += 'L'
#         lastNum = lst.popleft()
#     elif lastNum < last:
#         str += 'R'
#         lastNum = lst.pop()
#     else:
#         break
#
# print(len(str))
# print(str)

#강의방식

lt = 0
rt = len(lst)-1
lastNum = 0
tmp = list()
str = ""

while lt<=rt:
    if lst[lt] > lastNum:
        tmp.append((lst[lt],'L'))
    if lst[rt] > lastNum:
        tmp.append((lst[rt],'R'))

    if len(tmp) == 0:
        break

    tmp.sort()
    lastNum = tmp[0][0]
    str += tmp[0][1]

    if tmp[0][1] == 'L':
        lt += 1
    elif tmp[0][1] == 'R':
        rt -= 1
    tmp.clear()

print(len(str))
print(str)
