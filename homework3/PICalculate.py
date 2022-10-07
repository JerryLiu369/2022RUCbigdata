from random import random
from time import time

PI = 3.1415926535898

print("精度比较：")

total_count = 1000000

print("蒙特卡洛方法：")
in_circle = 0
for i in range(total_count):
    x, y = random() * 2 - 1, random() * 2 - 1
    if x ** 2 + y ** 2 <= 1:
        in_circle += 1
    if not i % (total_count // 10):
        print(in_circle / (i + 1) * 4)

print("莱布尼茨级数：")
pi_cal = 0
for i in range(total_count):
    pi_cal += (1 / (2 * i + 1)) * ((-1) ** i)
    if not i % (total_count // 10):
        print(pi_cal * 4)
print(pi_cal * 4)

print("\n时间比较:")

precision = 0.000001
print(f"精度为{precision:}")

print("蒙特卡洛方法：")
total_count = 0
in_circle = 0
begin = time()
while True:
    total_count += 1
    x, y = random() * 2 - 1, random() * 2 - 1
    if x ** 2 + y ** 2 <= 1:
        in_circle += 1
    if abs(in_circle / total_count * 4 - PI) < precision:
        end = time()
        print(f"计算时间为:{end - begin:.8f}")
        break

print("莱布尼茨级数：")
i = 0
pi_cal = 0
begin = time()
while True:
    pi_cal += (1 / (2 * i + 1)) * ((-1) ** i) * 4
    i += 1
    if abs(pi_cal - PI) < precision:
        end = time()
        print(f"计算时间为:{end - begin:.8f}")
        break
