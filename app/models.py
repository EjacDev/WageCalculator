import datetime
from typing import List

class WorkingHour:
    """Represents a time block for a specific date, and with a rate
    """
    def __init__(self,day:str, start_time:datetime.time, end_time:datetime.time,rate:int = 0) -> None:
        """Initialize the working hour

        Args:
            day (str): day of the schedule
            start_time (datetime.time): working hour start time 
            end_time (datetime.time): working hour end time
            rate (int, optional): rate for this working hour. Defaults to 0.
        """
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.rate = rate

    @staticmethod
    def get_by_day(day:str) -> List:
        """Return the list of rates for a specific day
            The hour `00:00` represents `24:00`, as the maximum,
            for example between `20:00` and `00:00` there is `4` hours.

        Args:
            day (str): day to get the rates

        Returns:
            List: list of working hours with the rate table
        """
        
        weekday_time_blocks = [
            WorkingHour(day, datetime.time(0, 0), datetime.time(9, 0), 25),
            WorkingHour(day, datetime.time(9, 0), datetime.time(18, 0), 15),
            WorkingHour(day, datetime.time(18, 0), datetime.time(0, 0), 20)
        ]
        weekend_time_blocks = [
            WorkingHour(day, datetime.time(0, 0), datetime.time(9, 0), 30),
            WorkingHour(day, datetime.time(9, 0), datetime.time(18, 0), 20),
            WorkingHour(day, datetime.time(18, 0), datetime.time(0, 0), 25)
        ]
        if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
            return weekday_time_blocks
        if day in ['Saturday', 'Sunday']:
            return weekend_time_blocks
        else:
            return list()

class Employee:
    """Represents a employee and their personal information
    """
    def __init__(self, name:str) -> None:
        self.name = name
        # Aditional personal employee information

class EmployeeSchedule(Employee):
    """Represents an employee with a related schule

    Args:
        Employee (_type_): _description_
    """
    def __init__(self, name:str, schedule:List[WorkingHour]) -> None:
        """_summary_

        Args:
            name (str): Name of the employee
            schedule (List[WorkingHour]): List of working hours as schedule
        """
        super().__init__(name)
        self.schedule = schedule



