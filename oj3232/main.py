"""กบน้อยกระโดด"""
x, y = map(int, input().split())
total_distance = 0
jumps = 0
while total_distance < y:
    if x <= 0:
        # ถ้าแรงกระโดดหมด (x <= 0) แต่ระยะทางรวมยังไม่ถึง y
        jumps = -1
        break
    total_distance += x
    jumps += 1
    x -= 2  # ระยะกระโดดลดลงครั้งละ 2 เมตร

print(jumps)
