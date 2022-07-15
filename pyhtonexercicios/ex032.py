#ano Bissexto
from datetime import date
year = int(input('enter any year to find out if it is a leap year: ,0 for year actual! '))
if year ==0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 ==0:
    print('Is a Leap Year!')
else:
    print('Is not Leap Year!')
print('The End')
# formula e condições novas
# biblioteca nova