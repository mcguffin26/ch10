import EmployeeClass as ec
import PayrollDeductionClass as pdc

def main():

    employee = ec.Employee('Jimmy Smith',58475,'Information Systems','Developer',6800.00)

    payroll_deductions = [['food court', '8/14/2022',22.50,39119],['gift contribution','8/12/2022',25.00,58475],
    ['food court','8/17/2022',15.25,21547],['vending machine','8/22/2022',3.00,58475],
    ['vending machine','8/5/2022',2.75,58475]]

    emp_charges = 0.0

    for row in payroll_deductions:
        if 58475 == row[3]:
            emp_charges += float(row[2])

    net_pay = employee.get_monthly_sal() - emp_charges

    print()
    print('*** Employee Pay ***')
    print('Name:', employee.get_name())
    print('ID Number:', employee.get_id_num())
    print('Department:', employee.get_dept())
    print('Gross Pay: $', format(employee.get_monthly_sal(), ',.2f'), sep='')
    print('Net Pay:$', format(net_pay, ',.2f'))
    print()

main()