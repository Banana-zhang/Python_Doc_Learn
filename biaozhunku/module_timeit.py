from timeit import Timer
out7 = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
print(out7)
out8 = Timer('a,b = b,a', 'a=1; b=2').timeit()
print(out8)