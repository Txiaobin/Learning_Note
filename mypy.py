import random
result = []
for i in range(101):
    result.append(0)
for i in range(1,1001):
    x = random.randint(1,100)
    result[i] = result[i] + 1
print(result)