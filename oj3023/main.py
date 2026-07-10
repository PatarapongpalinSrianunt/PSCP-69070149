'''Calculator'''
n = int(input())
if n == 1:
    print(n)
else:
    t = 0
    for i in range(1, n + 1 ):
        t += len(str(i))
    print(t+n)
