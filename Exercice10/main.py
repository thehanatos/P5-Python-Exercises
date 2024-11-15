class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"The person is {self.name}, {self.age} years old")


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        super().display_details()
        print(f"The salary is {self.salary}")


new_person = Person("Carrie", 17)
new_person.display_details()

new_employee = Employee("Eva", 28, 35000)
new_employee.display_details()
