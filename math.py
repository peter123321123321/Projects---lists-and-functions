import math


a = int(input("What is 'a'"))
b = int(input("What is 'b'"))
angle = int(input("What is the angle[Cos]"))
angle_degrees = angle*180/math.pi
answer = (a*a)+(b*b)-(2*a*b*angle_degrees)
print(answer)
