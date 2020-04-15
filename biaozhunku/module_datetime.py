# dates are easily constructed and formatted
from datetime import date
now = date.today()
print(now)

out6 = now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
print(out6)

# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
print(age.days)