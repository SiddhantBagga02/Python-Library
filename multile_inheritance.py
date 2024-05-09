class Student:
    def __init__(self, student_id):
        self.student_id = student_id

    def print_student_info(self):
        print("Student ID:", self.student_id)

class Employee:
    def __init__(self, employee_id):
        self.employee_id = employee_id

    def print_employee_info(self):
        print("Employee ID:", self.employee_id)

class Person(Student, Employee):
    def __init__(self, name, age, student_id, employee_id):
        super().__init__(student_id=student_id)
        Employee.__init__(self, employee_id=employee_id)
        self.name = name
        self.age = age

    def print_person_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


# person_instance = Person(name="John", age=25, student_id="S123", employee_id="E456")
person_instance = Person("sahil",20,11363,123)
person_instance.print_person_info()
person_instance.print_student_info()
person_instance.print_employee_info()

# a =  Student(11363)
# b = Employee(123)
# a.print_student_info()
# b.print_employee_info()