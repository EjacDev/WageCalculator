from app.models import WorkingHour
from app.filereader import FileReader
from app.calculator import WageCalculator

class Main:
    """Run the procceses and print the final result
    """
    
    def __init__(self, file_name:str, employees:list = list()):
        """Initialize the object

        Args:
            file_name (str): Filename to process
            employees (list, optional): Starts an empty list. Defaults to list().
        """
        self.file_reader = FileReader(file_name)
        self.employees = employees

    def load_file(self):
        """Process the file and update the employees list
        """ 
        try:
            self.employees = self.file_reader.read()
        except ValueError as e:
            print(f"Error: {e}")
        
    def calculate_all_schedules(self, employee):
        """Calculate the wage for the employee schedule
        """
        for working_hour in employee.schedule:
            calculator = WageCalculator(WorkingHour.get_by_day(working_hour.day))
            working_hour.rate = calculator.calculate_wage(working_hour.start_time, working_hour.end_time)

    def print_total_wage(self, employee):
        """Prints the total wage the employee
        """
        total = (int)(sum(working_hour.rate for working_hour in employee.schedule))
        print(f"The amount to pay {employee.name} is: {total} USD")            