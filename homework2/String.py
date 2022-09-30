import time
scale = 10
print("------执行开始------")
for i in range(scale + 1):
    a = "**" * i
    b = ".." * (scale - i)
    c=(i / scale) * 100
    print("%{0:^3.0f}[{1}->{2}]".format(c,a,b),end="\r")
    time.sleep(0.2)

print("\n------执行结束------")