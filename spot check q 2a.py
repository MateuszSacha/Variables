# mateusz sacha
# 29/09/2014
# stop check q 2a
weight= int(input("enter a weight"))
hundred= weight//100
remainder= weight % 100
fifty = remainder //50
remainder= remainder %50
ten = remainder // 10
remainder = remainder %10
five = remainder // 5
remainder= remainder %5
two = remainder //2
remainder = remainder %2
one = remainder
print("hundreds needed {0}, fifties needed {1}, tens needed{2}, fives needed {3}, twos needed {4}, ones needed {5}".format(hundred,fifty,ten,five,two,one))
