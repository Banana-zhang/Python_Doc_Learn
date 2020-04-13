import fibo
fibo.fib(1000)
print(fibo.fib2(100))
print(fibo.__name__)
# 导入模块的其他方式
from fibo import *      #  * 导入模块的全部关键字
fib(500)
print(fib2(1000))

import fibo as fib      # 导入模块里的fib关键字
fib.fib(500)

from fibo import fib as fibonacci       # 导入fib关键字，用fibonacci代替
fibonacci(500)