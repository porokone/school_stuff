user_name = input("Enter your name: ")
user_birthday = input("Enter your birthday (dd.mm.yyyy): ")
user_day, user_month, user_year = map(int, user_birthday.split('.'))
from datetime import datetime
day = datetime.now().day
month = datetime.now().month
year = datetime.now().year
if user_month < month or (user_month == month and user_day < day):
    age = year - user_year
else:
    age = year - user_year - 1
print(f"Hello, {user_name}! You are {age} years old.")
