import pytest
from datetime import time

from app.calculator import WageCalculator
from app.models import WorkingHour

def test_calculate_hours():
    """Test the time difference calculation
        The hour `00:00` represents `24:00` as the maximum,
        for example between `18:00` and `00:00` there is `6` hours.
    """
    assert WageCalculator.calculate_hours(time(1,0),time(10,0)) == 9
    assert WageCalculator.calculate_hours(time(0,0),time(0,0)) == 24
    assert WageCalculator.calculate_hours(time(18,0),time(0,0)) == 6
    assert WageCalculator.calculate_hours(time(0,0),time(10,0)) == 10
    assert WageCalculator.calculate_hours(time(0,0),time(23,0)) == 23

def test_calculate_wage():
    """Test different wage calculation applying diffent day rates
    """
    calculator = WageCalculator(WorkingHour.get_by_day("NoExists"))
    assert calculator.calculate_wage(time(0,0),time(0,0)) == 0
    calculator = WageCalculator(WorkingHour.get_by_day("Monday"))
    assert calculator.calculate_wage(time(0,0),time(0,0)) == 480
    assert calculator.calculate_wage(time(8,0),time(12,0)) == 70
    calculator = WageCalculator(WorkingHour.get_by_day("Tuesday"))
    assert calculator.calculate_wage(time(0,0),time(0,0)) == 480
    assert calculator.calculate_wage(time(18,0),time(0,0)) == 120
    calculator = WageCalculator(WorkingHour.get_by_day("Wednesday"))
    assert calculator.calculate_wage(time(0,0),time(0,0)) == 480
    assert calculator.calculate_wage(time(12,0),time(18,0)) == 90
    calculator = WageCalculator(WorkingHour.get_by_day("Thursday"))
    assert calculator.calculate_wage(time(0,0),time(0,0)) == 480
    assert calculator.calculate_wage(time(9,0),time(18,0)) == 135
    calculator = WageCalculator(WorkingHour.get_by_day("Friday"))
    assert calculator.calculate_wage(time(0,0),time(0,0)) == 480
    assert calculator.calculate_wage(time(0,0),time(1,0)) == 25
    calculator = WageCalculator(WorkingHour.get_by_day("Saturday"))
    assert calculator.calculate_wage(time(0,0),time(0,0)) == 600
    assert calculator.calculate_wage(time(10,0),time(12,0)) == 40