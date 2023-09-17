class Students(object):
    def __init__(self, idNo, grade):
        self._idNo = idNo
        self._grade = grade
 
    def __new__(cls, idNo, grade):
        print("Creating Instance")
        instance = super(Students, cls).__new__(cls)
        if 5 <= grade <= 10:
            return instance
        else:
            return None
 
    def __str__(self):
        return '{0}({1})'.format(self.__class__.__name__, self.__dict__)
 
 
stud1 = Students(1, 7)
print(stud1)
 
stud2 = Students(2, 12)
print(stud2)