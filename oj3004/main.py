'''3D'''
import math
a,b,c = map(int, input().split())
e,f,g = map(int, input().split())
point1 = [a, b, c]
point2 = [e, f, g]

distance = math.dist(point1, point2)
print(f"{distance:.2f}")
