#My first ever project to ever push into github.
#This is a simple script to find what day of an inputted date it is

from datetime import datetime

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

day_input = input("Enter the day date: ")
month_input = input("Enter the month (number): ")
year_input = input("Enter the year: ")

date = datetime.strptime(f"{year_input}-{month_input}-{day_input}", "%Y-%m-%d")
#idk what this part means but thx copilot ig

day_of_week = days[date.weekday()]
print(f"{year_input}-{month_input}-{day_input} is on {day_of_week}.")