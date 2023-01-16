import datetime
from typing import List

class WorkingHour:
    def __init__(self,day:str, start_time:datetime.time, end_time:datetime.time,rate:int = 0) -> None:
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.rate = rate

    @staticmethod
    def get_by_day(day:str) -> List:
        
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
    def __init__(self, name:str) -> None:
        self.name = name
        #Aditional personal employee information

class EmployeeSchedule(Employee):
    def __init__(self, name:str, schedule:List[WorkingHour]) -> None:
        super().__init__(name)
        self.schedule = schedule



