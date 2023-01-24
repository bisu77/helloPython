# if, 다중if

x=7
if x==7:
    print("Lucky")
    print("ㅋㅋ")

if x==7 and 1==1:
    print("true")

if 0<x<10:
    print("wow")

x=-1
if x>0:
    print("양수")
else:
    print("음수")

x=93
if x>=90:
    print("A")
elif x>=80:
    print("B")
elif x>=70:
    print("C")
else:
    print("F")

# for / while

a=range(1,11)
print(a)
print(list(a))

print("=================")

for i in range(10):
    print(i)

print("=================")
for i in range(10,0,-2):
    print(i)
print("=================")

for i in range(10,15):
    print(i)

print("=================")
i=1
while i<=10:
    print(i)
    i=i+1

print("=================")
i=1
while True:
    print(i)
    i+=1
    if i==10:
        break

for i in range(1,11):
    if i%2==0:
        continue
    print(i)

for i in range(1,11):
    print(i)
    if i==15:
        break
else:
    print(11)
