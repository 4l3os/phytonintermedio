#Datos
from datetime import datetime

now=datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

year_2023 = datetime(2023, 1, 1, 3)


print_date(year_2023)


timestamp= now.timestamp()
print(timestamp)



from datetime import time

current_time= time( 21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)



from datetime import date 

current_date= date.today( )

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date= date(2024,6,20 )

print(current_date.year)
print(current_date.month)
print(current_date.day)