from random import random

print("蒙特卡洛方法：")
total_count = 1000000
in_circle = 0
for i in range(total_count):
    x, y = random() * 2 - 1, random() * 2 - 1
    if x ** 2 + y ** 2 <= 1:
        in_circle += 1
    if not i % (total_count // 10):
        print(in_circle / (i + 1) * 4)

print("莱布尼茨级数：")
total_count = 1000000
pi_cal = 0
for i in range(total_count):
    pi_cal += (1 / (2 * i + 1)) * ((-1) ** i)
    if not i % (total_count // 10):
        print(pi_cal * 4)
print(pi_cal * 4)
