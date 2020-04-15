import re
output5 = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(output5)
output6 = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print(output6)

output7 = 'tea for too'.replace('too', 'two')
print(output7)