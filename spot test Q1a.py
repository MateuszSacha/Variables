# Mateusz Sacha
# 24/09/2014
# Assignment Statement Spot Check
width= int(input("enter the width of the pool"))
length= int(input("enter the length of the pool"))
depth= int(input("enter the depth of the pool"))
mainSectionVolume= width * length * depth
circleRadius = width/2
circleArea= 3.14 * circleRadius**2
halfCircleVolume = (circleArea / 2) * depth
poolVolume= mainSectionVolume + halfCircleVolume
print(poolVolume)
