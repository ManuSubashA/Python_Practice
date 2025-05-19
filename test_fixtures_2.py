import pytest


@pytest.fixture
def employee_data():
    return {
        "employee_name" : "Manu",
        "email" : "manu@virtusa.com",
        "age" : 27
    }
@pytest.fixture
def organization_data():
    return{
        "employee_id" : 9090435,
        "designation" : "Consultant",
        "Experience" : "5 years"
    }

def test_employee_data(employee_data):
    assert isinstance(employee_data, dict)
    assert employee_data["employee_name"] == "Manu"
    assert "email" in employee_data
    assert employee_data["age"] >18

def test_org_data(organization_data): 
    assert isinstance(organization_data, dict)
    assert organization_data["employee_id"] == 9090435
    assert organization_data["Experience"] >0