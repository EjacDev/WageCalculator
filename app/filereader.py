import os
import datetime
from app.models import EmployeeSchedule,WorkingHour

class FileReader:
    """Process the file 
    """
    def __init__(self, file_name:str) -> None:
        """initialize the object and set the filename

        Args:
            file_name (str): filename to process
        """
        self.file_name = file_name

    def read(self):
        """Read the file and create the list of EmployeeSchedule

        Returns:
            List: List of EmployeeSchedule from the file
        """
        _, file_ext = os.path.splitext(self.file_name)
        if file_ext != ".txt":
            raise ValueError(f"Invalid file format: {file_ext}. Only .txt files are supported.")
        employees = list()
        schedule_parser = ScheduleParser()
        try:
            with open(self.file_name, "r") as file:
                for line in file:
                    try:
                        if "=" not in line:
                            raise ValueError("Invalid name separator.")
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
    """Parse the schedule string from file, to a list of objects
    """
    def __init__(self) -> None:
        """set the days abbreviations
        """
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

    def parse_schedule_string(self, schedule_string:str):
        """Parse the schedule string from file, to a object list

        Args:
            schedule_string (str): Schedule string from file

        Returns:
            List(WorkingHour): List of the full employee schedule
        """
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
                if start_time > end_time and end_time != datetime.time(0,0):
                    raise ValueError(f"Start time cannot be greater than end time.")
                working_hour = WorkingHour(day, start_time, end_time)
                self.check_repeated_hours(working_hour,schedule)
                schedule.append(working_hour)
            except ValueError as error:
                raise ValueError(f"Invalid time format for the schedule: {time_range}. Error: {error}")
        return schedule

    def check_repeated_hours(self, current_working_hour, schedule):
        """Check if the current_working_hour has a conflict with another schedule

        Args:
            current_working_hour (WorkingHour): Current working hour to compare
            schedule (List(WorkingHour)): List of the current schedule
        """
        for working_hour in schedule:
            if current_working_hour.day == working_hour.day and current_working_hour.end_time > working_hour.start_time and current_working_hour.start_time < working_hour.end_time:
                    raise ValueError(f"There are duplicated working hours.")