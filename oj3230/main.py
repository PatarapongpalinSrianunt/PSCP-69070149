"""โรงแรมกลางกรุง ไม่มีชั้น 13"""
n = input().strip()
d1 = int(n[0])
d2 = int(n[1])
d3 = int(n[2])
d4 = int(n[3])
d5 = int(n[4])

if d1 > 5:
    X = "9"
elif d2 > 5:
    X = "10"
elif d3 > 5:
    X = "11"
elif d4 > 5:
    X = "12"
elif d5 > 5:
    X = "14"
else:
    X = "13"

if n == n[::-1]:
    if d1 + d5 > 5:
        Y = "1"
    elif d2 * d4 > 5:
        Y = "2"
    else:
        Y = "0"
else:
    if d5 and d1 // d5 > 5:
        Y = "1"
    elif d2 - d5 > 5:
        Y = "2"
    else:
        Y = "0"

total_sum = d1 + d2 + d3 + d4 + d5
total_prod = d1 * d2 * d3 * d4 * d5

if total_sum > 25:
    Z = "1"
elif total_prod > 55:
    Z = "2"
else:
    Z = "0"

print(X + Y + Z)
