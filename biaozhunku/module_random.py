import random
out3 = random.choice(['apple', 'pear', 'banana'])
print(out3)
out4 = random.sample(range(100), 10)   # sampling without replacement
print(out4)
out5 = random.random()    # random float
print(out5)
out6 = random.randrange(6)    # random integer chosen from range(6)
print(out6)
