#중첩 반복문

for i in range(5):
    print('i:',i, end=' ')
    for j in range(5):
        print('j:',j, end= ' ')
    print()


for i in range(5):
    for j in range(5-i):
        print('*', end=' ')
    print()