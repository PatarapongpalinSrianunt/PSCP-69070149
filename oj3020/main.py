"""calculated new promotion coke"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())

CAPS = 0
SUMC = 0

for i in range(d):
    i += 0
    if 0 < b <= CAPS:
        SUMC += c
        CAPS -= b
    else:
        SUMC += a
    CAPS += 1

print(SUMC)
