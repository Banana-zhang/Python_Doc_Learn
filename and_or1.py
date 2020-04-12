
'''比较操作符 in 和 not in 校验一个值是否在（或不在）一个序列里。
操作符 is 和 is not 比较两个对象是不是同一个对象，这只对像列表这样的可变对象比较重要。
所有的比较操作符都有相同的优先级，且这个优先级比数值运算符低。

比较操作可以传递。例如 a < b == c 会校验是否 a 小于 b 并且 b 等于 c。

比较操作可以通过布尔运算符 and 和 or 来组合，
并且比较操作（或其他任何布尔运算）的结果都可以用 not 来取反。
这些操作符的优先级低于比较操作符；
在它们之中，not 优先级最高， or 优先级最低，
因此 A and not B or C 等价于 (A and (not B)) or C。
和之前一样，你也可以在这种式子里使用圆括号。

布尔运算符 and 和 or 也被称为 短路 运算符：
它们的参数从左至右解析，一旦可以确定结果解析就会停止。
例如，如果 A 和 C 为真而 B 为假，那么 A and B and C 不会解析 C。
当用作普通值而非布尔值时，短路操作符的返回值通常是最后一个变量。'''

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)

(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)