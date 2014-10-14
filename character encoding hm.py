# Mateusz Sacha
# 14-10-2014
# character encoding homework
test = "1000001"
sixty_four = int(test[0])*64
print(sixty_four)
thirty_two = int(test[1])*32
print(thirty_two)
sixteen = int(test[2])*16
print(sixteen)
eight = int(test[3])*8
print(eight)
four = int(test[4])*4
print(four)
two = int(test[5])*2
print(two)
one = int(test[6])*1
print(one)
ascii_code=(sixty_four + thirty_two + sixteen + eight + four + two + one)
print(chr(ascii_code))



