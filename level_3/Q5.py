# Q5.py
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, other_time):
        total_minutes = (self.hours * 60 + self.minutes) + (other_time.hours * 60 + other_time.minutes)
        return Time(total_minutes // 60, total_minutes % 60)

    def displayTime(self):
        print(f"{self.hours} hours and {self.minutes} minutes")

    def displayMinute(self):
        total_minutes = self.hours * 60 + self.minutes
        print(f"{total_minutes} minutes")

# Example usage
if __name__ == "__main__":
    time1 = Time(2, 50)
    time2 = Time(1, 20)
    added_time = time1.addTime(time2)
    added_time.displayTime()
    added_time.displayMinute()
