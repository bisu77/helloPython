#반복문을 이용한 문제풀이

## 1) 1부터 N까지 홀수 출력
n = int(input("숫자를 입력하세요"))
for i in range(1,n+1):
    if i%2==1:
        print(i)

## 2) 1부터 N까지 합
n = int(input("숫자를 입력하세요"))
result = 0
for i in range(1,n+1):
    result+=i
else:
    print(result)

## 3) N의 약수 출력하기
n = int(input("숫자를 입력하세요"))
for i in range(1,n+1):
    if n%i==0:
        print(i, end=' ')