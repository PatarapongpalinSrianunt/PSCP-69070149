'''Rabbit chok pun'''

a,b,c = map(int, input().split())
price = int(input())

T = (a + b) * 2
C = T * c
OVER = price * C

print(C)
print(OVER)
