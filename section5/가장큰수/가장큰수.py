# 선생님은 현수에게 숫자 하나를 주고, 해당 숫자의 자릿수들 중 m개의 숫자를 제거하여 가장 큰 수를 만들라고 했습니다.
# 여러분이 현수를 도와주세요.(단 숫자의 순서는 유지해야 합니다)
#
# 만약 5276823 이 주어지고 3개의 자릿수를 제거한다면 7823이 가장 큰 숫자가 됩니다.
#
# ▣ 입력설명
# 첫째 줄에 숫자(길이는 1000을 넘지 않습니다)와 제가해야할 자릿수의 개수가 주어집니다.
#
# ▣ 출력설명
# 가장 큰 수를 출력합니다.

import sys

sys.stdin = open("가장큰수.txt", "rt")

#강의방식
num, M = map(int, input().split())

num = list(map(int, str(num)))
stack = []

for val in num:
    while stack and M > 0 and stack[-1] < val:
        stack.pop()
        M -= 1

    stack.append(val)

if M > 0:
    stack = stack[:-M]

print(''.join(map(str,stack)))


#내 방식
# N, M = map(str, input().split())
#
# stack = list()
# M = int(M)
# isBrake = False
# idx = 0
#
# for val in N:
#     idx += 1
#     if len(stack) == 0:
#         stack.append(val)
#         continue
#
#     while len(stack) > 0 and stack[-1] < val:
#         stack.pop()
#         M -= 1
#         if M == 0:
#             isBrake = True
#             break
#
#     stack.append(val)
#
#     if isBrake:
#         for val2 in N[idx:]:
#             stack.append(val2)
#         break
#
# while M > 0:
#     stack.pop()
#     M -= 1
#
# print(''.join(stack))


