import datetime
import pytest

from filereader import FileReader, ScheduleParser

def test_schedule_parser():
    schedule_parser = ScheduleParser()
    schedule_string = "MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00"
    schedules = schedule_parser.parse_schedule(schedule_string)
    assert len(schedules) == 5
    assert schedules[0].days == "Monday"
    assert schedules[0].start_time == datetime.time(10, 0)
    assert schedules[0].end_time == datetime.time(12, 0)
    assert schedules[1].days == "Tuesday"
    assert schedules[1].start_time == datetime.time(10, 0)
    assert schedules[1].end_time == datetime.time(12, 0)
    assert schedules[2].days == "Thursday"
    assert schedules[2].start_time == datetime.time(1, 0)
    assert schedules[2].end_time == datetime.time(3, 0)
    assert schedules[3].days == "Saturday"
    assert schedules[3].start_time == datetime.time(14, 0)
    assert schedules[3].end_time == datetime.time(18, 0)
    assert schedules[4].days == "Sunday"
    assert schedules[4].start_time == datetime.time(20, 0)
    assert schedules[4].end_time == datetime.time(21, 0)
    with pytest.raises(ValueError, match="Invalid day: 'AB'"):
        schedule_parser.parse_schedule("AB10:00-12:00")
    with pytest.raises(ValueError, match="Invalid time format for schedule: 12-13. time data '12' does not match format '%H:%M'"):
        schedule_parser.parse_schedule("MO12-13")


def test_file_loader():
    file_loader = FileReader("data.txt")
    people = file_loader.load()
    assert len(people) == 2
    assert people[0].name == "RENE"
    assert len(people[0].schedule) == 5
    assert people[0].schedule[0].days == "Monday"
    assert people[0].schedule[0].start_time == datetime.time(10, 0)
    assert people[0].schedule[0].end_time == datetime.time(12, 0)
    assert people[0].schedule[1].days == "Tuesday"
    assert people[0].schedule[1].start_time == datetime.time(10, 0)
    assert people[0].schedule[1].end_time == datetime.time(12, 0)
    assert people[0].schedule[2].days == "Thursday"
    assert people[0].schedule[2].start_time == datetime.time(1, 0)
    assert people[0].schedule[2].end_time == datetime.time(3, 0)
    assert people[0].schedule[3].days == "Saturday"
    assert people[0].schedule[3].start_time == datetime.time(14, 0)
    assert people[0].schedule[3].end_time == datetime.time(18, 0)
    assert people[0].schedule[4].days == "Sunday"
    assert people[0].schedule[4].start_time == datetime.time(20, 0)
    assert people[0].schedule[4].end_time == datetime.time(21, 0)
    with pytest.raises(ValueError, match="File not found: schedule_not_exist. \\[Errno 2\\] No such file or directory: 'schedule_not_exist'"):
        file_loader = FileReader("schedule_not_exist")
        file_loader.load()