"""สลากกินแบ่ง"""
winning_prefix, winning_num = input().split()
my_prefix, my_num = input().split()

is_prefix_match = winning_prefix == my_prefix
is_full_num_match = winning_num == my_num
is_last2_match = winning_num[-2:] == my_num[-2:]
is_last3_match = winning_num[-3:] == my_num[-3:]

if is_prefix_match and is_full_num_match:
    PRIZE = 1000000
elif is_full_num_match:
    PRIZE = 100000
elif is_prefix_match and is_last3_match:
    PRIZE = 2000
elif is_prefix_match and is_last2_match:
    PRIZE = 1000
elif is_last3_match:
    PRIZE = 200
elif is_last2_match:
    PRIZE = 100
elif is_prefix_match:
    PRIZE = 20
else:
    PRIZE = 0

print(PRIZE)
