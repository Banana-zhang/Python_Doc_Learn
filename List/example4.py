# 列表推导式的两种写法：
# 1
squares = list(map(lambda x: x**2, range(10)))
print(squares)
# 2
squares2 = [x**2 for x in range(10)]
print(squares2)