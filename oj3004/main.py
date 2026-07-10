'''3D'''
import math
a,b,c = map(int, input().split())
e,f,g = map(int, input().split())

d = math.sqrt(((a-e)**2)+((b-f)**2)+((c-g)**2))
print(f"{d:.2f}")
