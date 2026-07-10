"""swap num"""
num = int(input())
s = input()
N = str(num)
T = N[::-1]
R = int(T)

if s == "+":
    result = num + R
    print(f"{num} {"+"} {R} {"="} {result}")
else:
    result = num * R
    print(f"{num} {"*"} {R} {"="} {result}")
