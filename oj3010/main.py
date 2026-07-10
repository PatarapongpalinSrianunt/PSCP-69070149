'''Quadrant'''
x = int(input())
y = int(input())

if x > 0 < y :
    print("Q1")
elif not x and not y:
    print("O")
elif x < 0 < y:
    print("Q2")
elif x < 0 > y:
    print("Q3")
elif not y :
    print("X")
elif not x :
    print("Y")
else:
    print("Q4")
