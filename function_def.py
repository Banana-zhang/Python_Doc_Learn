def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(1000)

"""函数的 执行 会引入一个用于函数局部变量的新符号表。 
更确切地说，函数中所有的变量赋值都将存储在局部符号表中；
而变量引用会首先在局部符号表中查找，
然后是外层函数的局部符号表，再然后是全局符号表，
最后是内置名称的符号表。 
因此，全局变量和外层函数的变量不能在函数内部直接赋值
（除非是在 global 语句中定义的全局变量，或者是在 nonlocal 语句中定义的外层函数的变量），
尽管它们可以被引用。"""