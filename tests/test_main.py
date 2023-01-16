import pytest

from app.run import Main

def test_load_file(capsys):
    """Test a correct file readed
    """
    main = Main("tests/data_test.txt")
    main.load_file()
    captured = capsys.readouterr()
    assert captured.out == ""

def test_load_file_invalid(capsys):
    """Test the output of a file not found
    """
    main = Main("not_exists.txt")
    main.load_file()
    captured = capsys.readouterr()
    assert captured.out == "Error: File not found: not_exists.txt. Error: [Errno 2] No such file or directory: 'not_exists.txt'\n"

def test_print_total(capsys):
    """Test the output of a the final result
    """
    main = Main("tests/data_test.txt")
    main.load_file()
    for employee in main.employees:
        main.calculate_all_schedules(employee)
    main.print_total_wage(main.employees[0])
    captured = capsys.readouterr()
    assert captured.out == "The amount to pay RENE is: 215 USD\n"
    main.print_total_wage(main.employees[1])
    captured = capsys.readouterr()
    assert captured.out == "The amount to pay ASTRID is: 85 USD\n"
    main.print_total_wage(main.employees[2])
    captured = capsys.readouterr()
    assert captured.out == "The amount to pay ERIK is: 365 USD\n"
    main.print_total_wage(main.employees[3])
    captured = capsys.readouterr()
    assert captured.out == "The amount to pay JHONY is: 220 USD\n"
    main.print_total_wage(main.employees[4])
    captured = capsys.readouterr()
    assert captured.out == "The amount to pay MARIA is: 480 USD\n"
    main.print_total_wage(main.employees[5])
    captured = capsys.readouterr()
    assert captured.out == "The amount to pay JEAN is: 600 USD\n"
    main.print_total_wage(main.employees[6])
    captured = capsys.readouterr()
    assert captured.out == "The amount to pay DAVID is: 90 USD\n"

def test_calculate_wage_by_day():
    """Tests the calculation of specific wages"""
    main = Main("tests/data_test.txt")
    main.load_file()
    main.calculate_all_schedules(main.employees[0])
    assert main.employees[0].schedule[0].rate == 30.0
    assert main.employees[0].schedule[1].rate == 30.0
    assert main.employees[0].schedule[2].rate == 50.0
    assert main.employees[0].schedule[3].rate == 80.0