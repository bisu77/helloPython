# 자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요.
# 만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다.
# 제한시간은 1초입니다.
#
# ▣ 입력설명
# 첫 줄에 자연수의 개수 N(2<=N<=200,000)이 주어집니다.
#
# ▣ 출력설명
# 첫 줄에 소수의 개수를 출력합니다.

# ▣ 입력예제 1
# 20
#
# ▣ 출력예제 1
# 8
def isPrime(num):
    if num == 1:
        return False

    for i in range(2, num//2+1):
        if num % i == 0:
            return False
    return True


import sys

sys.stdin = open('소수.txt', 'rt')

N = int(input())
# result = 0
#
# for i in range(1,N+1):
#     if isPrime(i):
#         result+=1
#
# print(result)

l = [0] * (N + 1)
cnt = 0

for i in range(2, N+1):
    if l[i] == 0:
        cnt+=1
        for j in range(i, N+1, i):
            l[j] += 1

print(cnt)