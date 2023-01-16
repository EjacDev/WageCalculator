import datetime
from typing import List

class WageCalculator:
    """Calculate the corresponding wage for a working hour
    """
    def __init__(self, working_hours:List) -> None:
        """Set the 'strategy' or rate table to calculate the wage

        Args:
            working_hours (List): List of working_hours with the rates
        """
        self.working_hours = working_hours

    def calculate_wage(self, start_time:datetime.time, end_time:datetime.time) -> int:
        """Calculate the wage applying the current 'strategy'

        Args:
            start_time (datetime.time): employee working hour start time 
            end_time (datetime.time): employee working hour end time

        Returns:
            int: Wage
        """
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
        """Calculate the hours difference between two times
            The hour `00:00` represents `24:00`, as the maximum,
            for example between `20:00` and `00:00` there is `4` hours.
            
        Args:
            start_time (datetime.time): working hour start time 
            end_time (datetime.time): working hour end time

        Returns:
            float: Total hour difference
        """
        sample_date = datetime.date(1,1,1)
        start_time = datetime.datetime.combine(sample_date, start_time)
        if end_time == datetime.time(0, 0):
            sample_date = datetime.date(1,1,2)
        end_time = datetime.datetime.combine(sample_date, end_time)
        return (end_time - start_time).total_seconds() / (60*60)

