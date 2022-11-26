
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
    
    def __repr__(self):
        return("Employee('{}', '{}', {})".format(self.first, self.last, self.pay))

    def __str__(self):
        return('{} - {}'.format(self.fullname(),self.email))

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay =emp_str.split('-')  
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer("Ngoc", "Van", 2000, 'Python')
dev_2 = Developer("phong", "an", 3000, 'C++')

mgr_1 = Manager("sue", "alex", 900, [dev_1])

emp_1 = Employee('viet', 'nam', 5000)
emp_2 = Employee('ha', 'noi', 2900)

print(emp_1)
print(repr(emp_1)) # = print(emp_1.__repr__())

print(str(emp_1)) # = print(emp_1.__str__())

print(int.__add__(1,2))
print(str.__add__('a','b'))
print(emp_1+emp_2)

print('test'.__len__())
print(emp_1.__len__())