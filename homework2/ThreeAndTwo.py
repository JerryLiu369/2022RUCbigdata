ratio = 0.001
res = 1
for i in range(365):
    if i % 5 in [0, 1, 2]:
        res *= 1 + ratio
    else:
        res *= 1 - ratio
print(f"结果：{res:}")
