'''集合是由不重复元素组成的无序的集。
它的基本用法包括成员检测和消除重复元素。
集合对象也支持像 联合，交集，差集，对称差分等数学运算。'''

'''花括号或 set() 函数可以用来创建集合。注意：
要创建一个空集合你只能用 set() 而不能用 {}，因为后者是创建一个空字典.'''

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

'orange' in basket                 # fast membership testing
print(basket)
'crabgrass' in basket
print(basket)

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print(a)                                  # unique letters in a

print(a - b)                              # letters in a but not in b

print(a | b)                              # letters in a or b or both

print(a & b)                              # letters in both a and b

print(a ^ b)                              # letters in a or b but not both


ww = {x for x in 'abracadabra' if x not in 'abc'}
print(ww)