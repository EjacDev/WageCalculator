import datetime
from models import EmployeeSchedule,WorkingHour


class FileReader:
    def __init__(self, file_name:str) -> None:
        self.file_name = file_name

    def read(self):
        employees = list()
        schedule_parser = ScheduleParser()
        try:
            with open(self.file_name, "r") as file:
                for line in file:
                    try:
                        name, schedule_string = line.strip().split("=",1)
                        if not name.isalpha() or len(name) == 0:
                            raise ValueError(f"Invalid employee name: '{name}'.")
                        schedule = schedule_parser.parse_schedule_string(schedule_string)
                        employee = EmployeeSchedule(name, schedule)
                        employees.append(employee)
                    except ValueError as error:
                        raise ValueError(f"Invalid line in the file: {line} Error: {error}")
        except FileNotFoundError as error:
            raise ValueError(f"File not found: {self.file_name}. Error: {error}")
        return employees



class ScheduleParser:
    def __init__(self) -> None:
        self.days = {
            "MO": "Monday",
            "TU": "Tuesday",
            "WE": "Wednesday",
            "TH": "Thursday",
            "FR": "Friday",
            "SA": "Saturday",
            "SU": "Sunday",
        }
        self.hour_format = "%H:%M"

    def parse_schedule_string(self, schedule_string):
        shifts = schedule_string.split(",")
        schedule = list()
        for shift in shifts:
            day, time_range = shift[:2],shift[2:]
            if day not in self.days:
                raise ValueError(f"Invalid day: '{day}'.")
            day = self.days[day]
            try:
                start_time, end_time = time_range.split("-",1)
                start_time = datetime.datetime.strptime(start_time, self.hour_format).time()
                end_time = datetime.datetime.strptime(end_time, self.hour_format).time()
                if start_time > end_time and end_time != datetime.datetime.time(0,0):
                    raise ValueError(f"Start time cannot be greater than end time.")
                schedule.append(WorkingHour(day, start_time, end_time))
            except ValueError as error:
                raise ValueError(f"Invalid time format for the schedule: {time_range}. Error: {error}")
        return schedule