
class Employee:
    
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay *Employee.raise_amount)


emp_1 = Employee("Ngoc", "Van", 2002)
print(emp_1.email)
print(emp_1.fullname())

print(emp_1.pay)
