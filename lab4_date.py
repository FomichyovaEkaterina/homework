import datetime
#Task1
current_date = datetime.datetime.now()
new_date = current_date - datetime.timedelta(days=5)
print("Date 5 days ago:", new_date.strftime("%Y-%m-%d"))

#Task2
yest = current_date - datetime.timedelta(days=1)
today = current_date
tom = current_date + datetime.timedelta(days=1)
print("Yesterday:", yest.strftime("%Y-%m-%d"))
print("Today:", today.strftime("%Y-%m-%d"))
print("Tomorrow:", tom.strftime("%Y-%m-%d"))

#Task3
print("Without microseconds:", today.strftime("%Y-%m-%d"), today.strftime("%H:%M:%S"))

#Task4
from datetime import datetime, timedelta
today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
yest = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
def date_difference_in_seconds(date1_str, date2_str, date_format="%Y-%m-%d %H:%M:%S"):
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)
    difference = date2 - date1
    return difference.total_seconds()
seconds_difference = date_difference_in_seconds(yest, today)
print(f"The difference between the two dates is {seconds_difference} seconds.")

