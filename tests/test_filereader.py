import datetime
import pytest

from app.filereader import ScheduleParser,FileReader 

def test_schedule_parser_invalid():
    schedule_parser = ScheduleParser()
    with pytest.raises(ValueError, match="Invalid day: 'AB'"):
        schedule_parser.parse_schedule_string("AB10:00-12:00")
    with pytest.raises(ValueError, match="Invalid time format for the schedule: 12-13. Error: time data '12' does not match format '%H:%M'"):
        schedule_parser.parse_schedule_string("MO12-13")
    with pytest.raises(ValueError, match="Invalid time format for the schedule: 1200-1300. Error: time data '1200' does not match format '%H:%M'"):
        schedule_parser.parse_schedule_string("MO1200-1300")
    with pytest.raises(ValueError, match="Invalid day: ''"):
        schedule_parser.parse_schedule_string("")
    with pytest.raises(ValueError, match="Invalid time format for the schedule: 09:00-08:00. Error: Start time cannot be greater than end time."):
        schedule_parser.parse_schedule_string("MO09:00-08:00")
    with pytest.raises(ValueError, match="Invalid time format for the schedule: 10:00-16:00. Error: There are duplicated working hours."):
        schedule_parser.parse_schedule_string("SA14:00-18:00,SA10:00-16:00")
    with pytest.raises(ValueError, match="Invalid day: '14'."):
        schedule_parser.parse_schedule_string("14:00-18:00")
    with pytest.raises(ValueError, match="Invalid time format for the schedule: N14:00-18:0. Error: time data 'N14:00' does not match format '%H:%M'"):
        schedule_parser.parse_schedule_string("MON14:00-18:0,#120")


def test_schedule_parser():
    schedule_parser = ScheduleParser()
    schedule_string = "MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00"
    schedules = schedule_parser.parse_schedule_string(schedule_string)
    assert len(schedules) == 5
    assert schedules[0].day == "Monday"
    assert schedules[0].start_time == datetime.time(10, 0)
    assert schedules[0].end_time == datetime.time(12, 0)
    assert schedules[1].day == "Tuesday"
    assert schedules[1].start_time == datetime.time(10, 0)
    assert schedules[1].end_time == datetime.time(12, 0)
    assert schedules[2].day == "Thursday"
    assert schedules[2].start_time == datetime.time(1, 0)
    assert schedules[2].end_time == datetime.time(3, 0)
    assert schedules[3].day == "Saturday"
    assert schedules[3].start_time == datetime.time(14, 0)
    assert schedules[3].end_time == datetime.time(18, 0)
    assert schedules[4].day == "Sunday"
    assert schedules[4].start_time == datetime.time(20, 0)
    assert schedules[4].end_time == datetime.time(21, 0)


def test_file_loader_invalid():
    with pytest.raises(ValueError, match="File not found: schedule_not_exist. Error: \\[Errno 2\\] No such file or directory: 'schedule_not_exist'"):
        file_loader = FileReader("schedule_not_exist")
        file_loader.read()
    with pytest.raises(ValueError, match="Invalid line in the file: RENEMO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\n Error: Invalid name separator."):
        file_loader = FileReader("tests/data_test_invalid.txt")
        file_loader.read()
    with pytest.raises(ValueError, match="Invalid line in the file: =MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\n Error: Invalid employee name: ''."):
        file_loader = FileReader("tests/data_test_invalid2.txt")
        file_loader.read()
    with pytest.raises(ValueError, match="Invalid line in the file: RENE=MO10:00-12:00,MO08:00-11:00\n Error: Invalid time format for the schedule: 08:00-11:00. Error: There are duplicated working hours."):
        file_loader = FileReader("tests/data_test_invalid3.txt")
        file_loader.read()

def test_file_loader():
    file_loader = FileReader("tests/data_test.txt")
    employees = file_loader.read()
    assert len(employees) == 2
    assert employees[0].name == "RENE"
    assert len(employees[0].schedule) == 5
    assert employees[0].schedule[0].day == "Monday"
    assert employees[0].schedule[0].start_time == datetime.time(10, 0)
    assert employees[0].schedule[0].end_time == datetime.time(12, 0)
    assert employees[0].schedule[1].day == "Tuesday"
    assert employees[0].schedule[1].start_time == datetime.time(10, 0)
    assert employees[0].schedule[1].end_time == datetime.time(12, 0)
    assert employees[0].schedule[2].day == "Thursday"
    assert employees[0].schedule[2].start_time == datetime.time(1, 0)
    assert employees[0].schedule[2].end_time == datetime.time(3, 0)
    assert employees[0].schedule[3].day == "Saturday"
    assert employees[0].schedule[3].start_time == datetime.time(14, 0)
    assert employees[0].schedule[3].end_time == datetime.time(18, 0)
    assert employees[0].schedule[4].day == "Sunday"
    assert employees[0].schedule[4].start_time == datetime.time(20, 0)
    assert employees[0].schedule[4].end_time == datetime.time(21, 0)