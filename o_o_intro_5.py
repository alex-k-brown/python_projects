7:44 PM

class Time(object):
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return "%d:%d:%d" %(self.hours, self.minutes, self.seconds)

    def __cmp__(self, other):
        left_time = self.hours *10000 + self.minutes * 100 + self.seconds
        right_time = other.hours *10000 + other.minutes * 100 + other.seconds
        if left_time < right_time:
            return -1
        elif left_time > right_time:
            return 1
        else:
            return 0