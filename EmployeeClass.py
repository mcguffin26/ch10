class Employee:
    def __init__(self,name,id_num,dept,job_title,monthly_sal):
        self.name = name
        self.id_num = id_num
        self.dept = dept
        self.job_title = job_title
        self.monthly_sal = monthly_sal

    def get_name(self):
        return self.name
    
    def get_id_num(self):
        return self.id_num

    def get_dept(self):
        return self.dept
    
    def get_job_title(self):
        return self.job_title
    
    def get_monthly_sal(self):
        return self.monthly_sal