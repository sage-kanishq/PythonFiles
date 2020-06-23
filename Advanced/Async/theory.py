class Employee:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.email = firstname+"."+lastname+"@company.com"
    
    def fullname(self):
        return self.firstname+" "+self.lastname
        