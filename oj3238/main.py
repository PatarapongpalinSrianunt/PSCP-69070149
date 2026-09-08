"""วาด X-shape"""
raw_input = input().strip()
if " " in raw_input:
    parts = raw_input.split()
    x = int(parts[0])
    k = parts[1]
else:
    x = int(raw_input[:-1])
    k = raw_input[-1]

center_idx = x // 2
for i in range(x):
    row = ["-"] * x

    if k == "#":
        CHAR = "#"
    else:
        dist = abs(i - center_idx)
        CHAR = chr(ord(k) + dist)

    row[i] = CHAR
    row[x - 1 - i] = CHAR
    print("".join(row))
