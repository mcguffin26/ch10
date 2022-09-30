class PayrollDeduction:
    def __init__(self,desc,date,charge,emp_ID):
        self.desc = desc
        self.date = date
        self.charge = charge
        self.emp_ID = emp_ID
    
    def get_desc(self):
        return self.desc

    def get_date(self):
        return self.date
    
    def get_charge(self):
        return self.charge

    def get_emp_ID(self):
        return self.emp_ID