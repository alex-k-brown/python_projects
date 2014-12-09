from datetime import date
from calendar import timegm
from time import gmtime

current_time = timegm(gmtime())

with open('dates') as dates:
    for line in dates:

        line = float(line)
        formatted_time = date.fromtimestamp(line)


        time_difference = current_time - line
        SECONDS_IN_DAY = 86400
        days_difference = time_difference / SECONDS_IN_DAY
        days_difference = int(days_difference)
        print formatted_time, "happened", days_difference, "days ago"