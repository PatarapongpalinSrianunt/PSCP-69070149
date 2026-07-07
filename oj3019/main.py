"""DOC"""
char = input()
num = int(input())
C_CHAR = "H"
C_NUM = 4567

if char == C_CHAR and num == C_NUM:
    print("safe unlocked")
elif char == C_CHAR and num != C_NUM:
    print("safe locked - change digit")
elif char != C_CHAR and num == C_NUM:
    print("safe locked - change char")
else:
    print("safe locked")
