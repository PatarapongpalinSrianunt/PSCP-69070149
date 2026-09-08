"""inflation"""
n = int(float(input())*100)
k = int(input())
P = 381
for _ in range(k):
    n += (n*P) // 10000
print(f"{n//100}.{n%100:02d}")
