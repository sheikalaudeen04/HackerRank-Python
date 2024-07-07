import math 
AB = int(input())
BC = int(input())
MBC = str(round(math.degrees(math.atan2(AB,BC))))+chr(176)
print(MBC)
