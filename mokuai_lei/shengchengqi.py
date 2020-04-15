def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)


output2 = sum(i*i for i in range(10))                 # sum of squares
print(output2)
xvec = [10, 20, 30]
yvec = [7, 5, 3]
output3 = sum(x*y for x,y in zip(xvec, yvec))         # dot product
print(output3)

from math import pi, sin
sine_table = {x: sin(x*pi/180) for x in range(0, 91)}
print(sine_table)

data = 'golf'
output4 = list(data[i] for i in range(len(data)-1, -1, -1))
print(output4)