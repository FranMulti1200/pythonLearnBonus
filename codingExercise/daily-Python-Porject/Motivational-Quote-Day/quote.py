import random

from modules import functions
import time

day_week = time.strftime("%A")

if day_week == "Monday":
    print(f"It´s {day_week}! Time for some motivation!\n")
    print("Motivotional Quote of the Day.")
    quote_days = functions.get_quote()
    for quote_day in quote_days:
        if quote_day == '\n':
            quote_days.pop(quote_days.index(quote_day))

    quote_rand = random.randint(0,len(quote_days) - 1)

    print(str(quote_days[quote_rand]))
else:
    print(f"Today is {day_week}")