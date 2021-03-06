'''列表推导式的结构是由一对方括号所包含的以下内容：
一个表达式，后面跟一个 for 子句，然后是零个或多个 for 或 if 子句。 
其结果将是一个新列表，由对表达式依据后面的 for 和 if 子句的内容进行求值计算而得出。
举例来说，以下列表推导式会将两个列表中不相等的元素组合起来:
'''
# 1
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
# 2
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print(combs)