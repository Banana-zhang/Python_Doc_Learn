# 如果在循环内需要修改序列中的值（比如重复某些选中的元素），
# 推荐你先拷贝一份副本。对序列进行循环不代表制作了一个副本进行操作。
# 切片操作使这件事非常简单：
words = ['cat', 'window', 'defenestrate']
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) < 6:
        words.insert(0, w)
print(w)