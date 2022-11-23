
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return('{} {}'.format(self.first, self.last))

emp_1 = Employee("Ngoc", "Van", 2002)
print(emp_1.email)
print(emp_1.fullname())
