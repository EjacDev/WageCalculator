import datetime
from typing import List

class WageCalculator:
    def __init__(self, working_hours:List) -> None:
        self.working_hours = working_hours

    def calculate_wage(self, start_time:datetime.time, end_time:datetime.time) -> int:
        wage = 0
        current_end_time = end_time
        for working_hour in self.working_hours:

            if start_time < working_hour.start_time:
                start_time = working_hour.start_time
            if end_time > working_hour.end_time and working_hour.end_time != datetime.time(0, 0):
                current_end_time = working_hour.end_time
            elif end_time == datetime.time(0, 0):
                current_end_time = working_hour.end_time
            else:
                current_end_time = end_time

            if current_end_time < start_time and current_end_time != datetime.time(0, 0):
                continue
            hours = self.calculate_hours(start_time,current_end_time)
            wage += hours * working_hour.rate
            start_time = working_hour.end_time
        return wage
        
    @staticmethod  
    def calculate_hours(start_time, end_time):
        sample_date = datetime.date(1,1,1)
        start_time = datetime.datetime.combine(sample_date, start_time)
        if end_time == datetime.time(0, 0):
            sample_date = datetime.date(1,1,2)
        end_time = datetime.datetime.combine(sample_date, end_time)
        return (end_time - start_time).total_seconds() / (60*60)

