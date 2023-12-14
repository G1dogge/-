import random
t = []
for i in range(100):
    c = random.randint(0, 100)
    if c % 2 != 0:
        t.append(c)
print("Непарні цифри:", t)