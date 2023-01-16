from app.models import WorkingHour
from app.filereader import FileReader
from app.calculator import WageCalculator

class Main:
    
    def __init__(self, file_name, employees:list = list()):
        self.file_reader = FileReader(file_name)
        self.employees = employees

    def load_file(self):    
        try:
            self.employees = self.file_reader.read()
        except ValueError as e:
            print(f"Error: {e}")
        
    def print_total(self):
        for employee in self.employees:
            total = (int)(sum(working_hour.rate for working_hour in employee.schedule))
            print(f"The amount to pay {employee.name} is: {total} USD")

    def calculate_all_schedules(self):
        for employee in self.employees:
            for working_hour in employee.schedule:
                calculator = WageCalculator(WorkingHour.get_by_day(working_hour.day))
                working_hour.rate = calculator.calculate_wage(working_hour.start_time, working_hour.end_time)  
            