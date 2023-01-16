# 리스트와 내장함수(1)
import random
import random as r

a=[1,2,3,4,5]

#1~10까지 리스트
b=list(range(1,11))
print(b)

#리스트합치기
c=a+b
print(c)

#리스트 마지막 인덱스 뒤에 추가
a.append(6)
print(a)

#해당 인덱스에 추가
a.insert(3,7)
print(a)

#리스트 마지막 인덱스 삭제
a.pop()
print(a)

#해당 인덱스 삭제
a.pop(3)
print(a)

#해당 value 삭제
a.remove(4)
print(a)

#해당 value의 index 반환
print(a.index(5))

a=list(range(1,11))
print(a)

#리스트 합
print(sum(a))
#리스트 최대값
print(max(a))
#리스트 최소값
print(min(a))
#5랑 7중에 최소값
print(min(5,7))

#리스트 랜덤
r.shuffle(a)
print(a)

#리스트 역순정렬
a.sort(reverse=True)
print(a)

#리스트 순서정렬
a.sort()
print(a)

#리스트 초기화
a.clear()
print(a)