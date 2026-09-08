"""คะแนนเกม"""
base = int(input())
bonus = int(input())
days = int(input())
x = base + bonus
if days > 3:
    x = int(x * 1.5)
if x >= 1500:
    STATUS = 5
elif x >= 1000:
    STATUS = 4
elif x >= 500:
    STATUS = 3
elif x >= 200:
    STATUS = 2
else:
    STATUS = 1
if STATUS == 5 and days >= 7:
    S = 99
elif STATUS == 4 and bonus > 300:
    S = 88
else:
    S = 0
print(x)
print(STATUS)
print(S)
