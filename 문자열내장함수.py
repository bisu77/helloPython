#문자열과 내장함수

msg = "It is Time"
print(msg.upper())

tmp=msg.upper()
print(tmp)

print(tmp.find('T'))
print(tmp.count('T'))
print(msg)
print(msg[:2])
print(msg[3:5])
print(len(msg))
print(msg[1])

for i in range(len(msg)):
    print(msg[i], end='')

print()
for x in msg:
    print(x, end='')
print()


for x in msg:
    if x.isupper():
        print(x,end ='')

print()
for x in msg:
    if x.isalpha():
        print(x, end='')

print()

tmp ='AZ'
for x in tmp:
    print(ord(x))


tmp = 65
print(chr(tmp))