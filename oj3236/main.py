"""แฝดเทคกระต่ายน้อย"""
n = int(input().strip())
code1 = input().strip()
code2 = input().strip()

mismatch_count = 0
for i in range(n):
    sum_digit = int(code1[i]) + int(code2[i])
    if sum_digit != 9:
        mismatch_count += 1
if not mismatch_count:
    print("YES")
else:
    print(f"NO {mismatch_count}")
