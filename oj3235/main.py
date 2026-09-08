"""กระต่ายน้อยอ้วนอวบ"""
n = int(input())
overweight_count = 0
max_weight = -1
fattest_bunny = ""

for _ in range(n):
    name, weight_str = input().split()
    weight = int(weight_str)

    if weight > 15:
        overweight_count += 1

    if weight > max_weight:
        max_weight = weight
        fattest_bunny = name

print(overweight_count)
print(fattest_bunny)
