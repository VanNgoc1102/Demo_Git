
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

emp_1 = Employee("Ngoc", "Van", 2002)
print(emp_1.email)
