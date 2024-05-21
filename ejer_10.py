import math
def formula(g, h, v):
    v = math.sqrt(2*g*h)
  
    return v


values = input().split(":")
dist, gra = map(float, values)
v = formula(gra, dist, 0)
v = v * 3.6

if v > 120:
    print("MUERE")
else:
    print("SOBREVIVE")
