from decimal import *
r3 = round(Decimal('0.70') * Decimal('1.05'), 2)
print(r3)
r4 = round(.70 * 1.05, 2)
print(r4)
r5 = Decimal('1.00') % Decimal('.10')
print(r5)
r6 = 1.00 % 0.10
print(r6)

r7 = sum([Decimal('0.1')]*10) == Decimal('1.0')
print(r7)
r8 = sum([0.1]*10) == 1.0
print(r8)

r9 = Decimal(1) / Decimal(7)
print(r9)