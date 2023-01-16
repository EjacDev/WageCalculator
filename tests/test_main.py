import pytest

from app.run import Main

def test_load_file(capsys):
    main = Main("tests/data_test.txt")
    main.load_file()
    captured = capsys.readouterr()
    assert captured.out == ""

def test_load_file_invalid(capsys):
    main = Main("not_exists.txt")
    main.load_file()
    captured = capsys.readouterr()
    assert captured.out == "Error: File not found: not_exists.txt. Error: [Errno 2] No such file or directory: 'not_exists.txt'\n"

def test_print_total(capsys):
    main = Main("tests/data_test.txt")
    main.load_file()
    main.calculate_all_schedules()
    main.print_total()
    captured = capsys.readouterr()
    assert captured.out == "The amount to pay RENE is: 215 USD\nThe amount to pay ASTRID is: 85 USD\n"

def test_calculate_wage_by_day():
    main = Main("tests/data_test.txt")
    main.load_file()
    main.calculate_all_schedules()
    assert main.employees[0].schedule[0].rate == 30.0
    assert main.employees[0].schedule[1].rate == 30.0
    assert main.employees[0].schedule[2].rate == 50.0
    assert main.employees[0].schedule[3].rate == 80.0