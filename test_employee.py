
from employee import employee_details

def test_employee_details():
    result = employee_details("Vibha", "101", "IT", "30000")

    expected = (
        "Name: Vibha\n"
        "Employee ID: 101\n"
        "Department: IT\n"
        "Salary: 30000"
    )

    assert result == expected
