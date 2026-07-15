"""a"""
m = int(input())
d = int(input())

season = ["winter", "spring", "summer", "fall"]
i = m // 3
if not m % 3 and d < 21:
    i -= 1

if i > 3:
    i = 0

print(f"{season[i]}")
