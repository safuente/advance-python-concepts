import json

json_data = '''{
    "name": "Alice",
    "role": "CEO",
    "employees_in_charge": [
        {
            "name": "Bob",
            "role": "CTO",
            "employees_in_charge": [
                {
                    "name": "Charlie",
                    "role": "Lead Developer",
                    "employees_in_charge": [
                        {
                            "name": "David",
                            "role": "Junior Developer",
                            "employees_in_charge": []
                        }
                    ]
                },
                {
                    "name": "Eva",
                    "role": "DevOps Engineer",
                    "employees_in_charge": []
                }
            ]
        },
        {
            "name": "Fiona",
            "role": "CFO",
            "employees_in_charge": []
        }
    ]
}'''


# Recursive function to process the employee hierarchy
def print_employee_hierarchy(employee, level=0):

    print(" " * level + f"Name: {employee['name']}, Role: {employee['role']}")

    if "employees_in_charge" in employee and employee['employees_in_charge']:
       print(" " * level + f"Employees in charge of: {employee['name']}")
       for subemployee in employee['employees_in_charge']:
            print_employee_hierarchy(subemployee, level+1)


employee = json.loads(json_data)

print_employee_hierarchy(employee)
