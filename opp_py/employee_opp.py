
class Employee:
    
    num_of_emps = 0
    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

emp_1 = Employee("Ngoc", "Van", 2002)
emp_2 = Employee("phong", "an", 2003)

emp_str_1 = 'le-dat-1000'
emp_str_2 = 'hoang-thai-3000'
emp_str_3 = 'van-huy-7262'

first, last, pay =emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)

print(new_emp_1.email)
print(new_emp_1.pay)