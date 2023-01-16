# 함수만들기

def add(a,b):
    c=a+b
    print(c)

def returnAdd(a,b):
    return a+b, a-b

add(5,1)

print(returnAdd(3,2))

def isPrime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

a=[12,13,7,9,19]
for y in a:
    if isPrime(y):
        print("소수 :: ", y)

