#리스트와 내장함수(2)

#리스트 부분 출력
a = [23,12,36,53,19]
print(a[1:4])

print(len(a))


#리스트 원소 1건씩 loop
for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    if x%2==1:
        print(x, end= ' ')
print()

#리스트를 tuple로 출력
for x in enumerate(a):
    print(x)
print()

#리스트를 tuple로 출력
for x in enumerate(a):
    print(x[0], x[1])
print()

#리스트를 tuple로 출력
for index, value in enumerate(a):
    print(index, value)
print()

b=(1,2,3,4,5)

print(b[0])
# b[0]=7 # >>> tuple은 원소 변경 불가

#리스트 원소가 모두 60 미만
if all(60>x for x in a):
    print("모두 60 미만")

#리스트 원소가 하나라도 차이면 true
if any(20>x for x in a):
    print("하나라도 20 초과")


