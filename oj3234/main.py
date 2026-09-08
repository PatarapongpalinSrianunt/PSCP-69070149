"""สายไฟคริสต์มาส"""
colors = ["Red", "Green", "Blue"]
start_color, count_str = input().split()
count = int(count_str)

if start_color == "R":
    START_INDEX = 0
elif start_color == "G":
    START_INDEX = 1
else:
    START_INDEX = 2

result = []
for i in range(count):
    color_name = colors[(START_INDEX + i) % 3]
    result.append(color_name)

print(*result)
