import math
my_str1 = "cтрока"
my_str2 = -3, 77
my_str3 = 4 / 2
my_str4 = ["a", "2"]
my_str5 = round(10 / 3.0, 1)
my_str6 = 10 > 3.0
my_str7 = int(3.333)
my_str8 = math.sqrt(9)

list = [my_str1, my_str2, my_str3, my_str4, my_str5, my_str6, my_str7, my_str8]
for a in list:
    print(f'{a} is {type(a)}')
