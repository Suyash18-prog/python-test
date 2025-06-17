# Use the datetime module to display the current date, time, and calculate the number of days
# between two dates.

from datetime import datetime,timedelta

print(datetime.now())
date1 = datetime(2025, 6, 18)
date2 = datetime(2024, 6, 18)
days_in_between = (date1 - date2).days
print(f"Number of days between {date1.date()} and {date2.date()}: {days_in_between}")