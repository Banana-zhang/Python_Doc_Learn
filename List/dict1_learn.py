tel = {'jack':4098, 'sape':4139}

tel['guido'] = 4127     # 增加
print(tel)
print(tel['sape'])
del tel['sape']         # 删除
print(tel)
tel['irv'] = 4127       # 增加
print(tel)
tel['asp'] = 4127       # 字典的元素一样，关键字可以不同
print(tel)
tel['irv'] = 4111       # 重新给关键字赋值，可以改变关键字的值
print(tel)
print(list(tel))        # 列出关键字
print(sorted(tel))      # 排序列出关键字
print('guido' in tel)
print('guido' not in tel)

