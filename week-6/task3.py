class Person:
    def __init__(self, name):
        self._name = name

    def get_info(self):
        return f"Person: {self._name}"


class Student(Person):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

    def get_info(self):
        return f"Student: {self._name}, Major: {self.major}"


p = Person("John")
s = Student("Alice", "CS")

print(p.get_info())
print(s.get_info())
