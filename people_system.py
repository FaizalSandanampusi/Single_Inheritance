class Person:
    """Base class representing a person with basic attributes.
    
    Attributes:
        name (str): The person's name
        age (int): The person's age
        job (str): The person's job title
    """
    
    def __init__(self, name: str, age: int, job: str):
        """Initialize a Person instance.
        
        Args:
            name: The person's name
            age: The person's age
            job: The person's job title
        """
        self.name = name
        self.age = age
        self.job = job
    
    def get_details(self) -> str:
        """Get a formatted string of person's details.
        
        Returns:
            str: Formatted string containing name, age, and job
        """
        return f"Name: {self.name}, Age: {self.age}, Job: {self.job}"

class Student(Person):
    """Student class inheriting from Person.
    
    Adds grade attribute and overrides get_details method.
    
    Attributes:
        grade (str): The student's grade (e.g., "A", "B", etc.)
    """
    
    def __init__(self, name: str, age: int, job: str, grade: str):
        """Initialize a Student instance.
        
        Args:
            name: Student's name
            age: Student's age
            job: Student's job (usually "Student")
            grade: Student's grade
        """
        super().__init__(name, age, job)
        self.grade = grade
    
    def get_details(self) -> str:
        """Get formatted string of student's details including grade.
        
        Returns:
            str: Formatted string with student details
        """
        return f"{super().get_details()}, Grade: {self.grade}"

class Professor(Person):
    """Professor class inheriting from Person.
    
    Adds courses attribute and overrides get_details method.
    
    Attributes:
        courses (list): List of courses the professor teaches
    """
    
    def __init__(self, name: str, age: int, job: str, courses: list):
        """Initialize a Professor instance.
        
        Args:
            name: Professor's name
            age: Professor's age
            job: Professor's job (usually "Professor")
            courses: List of courses taught
        """
        super().__init__(name, age, job)
        self.courses = courses
    
    def get_details(self) -> str:
        """Get formatted string of professor's details including courses.
        
        Returns:
            str: Formatted string with professor details
        """
        return f"{super().get_details()}, Courses: {self.courses}"

class Employee(Person):
    """Employee class inheriting from Person.
    
    Adds department attribute and overrides get_details method.
    
    Attributes:
        department (str): The employee's department
    """
    
    def __init__(self, name: str, age: int, job: str, department: str):
        """Initialize an Employee instance.
        
        Args:
            name: Employee's name
            age: Employee's age
            job: Employee's job title
            department: Employee's department
        """
        super().__init__(name, age, job)
        self.department = department
    
    def get_details(self) -> str:
        """Get formatted string of employee's details including department.
        
        Returns:
            str: Formatted string with employee details
        """
        return f"{super().get_details()}, Department: {self.department}"

class StudentProfessor(Student, Professor):
    """Multiple inheritance class combining Student and Professor.
    
    Demonstrates multiple inheritance by combining attributes of both
    Student and Professor classes.
    """
    
    def __init__(self, name: str, age: int, job: str, courses: list, grade: str):
        """Initialize a StudentProfessor instance.
        
        Args:
            name: Name
            age: Age
            job: Job title
            courses: List of courses taught
            grade: Current grade as a student
        """
        Person.__init__(self, name, age, job)
        self.courses = courses
        self.grade = grade
    
    def get_details(self) -> str:
        """Get formatted string combining student and professor details.
        
        Returns:
            str: Formatted string with combined details
        """
        return f"Name: {self.name}, Age: {self.age}, Job: {self.job}, Courses: {self.courses}, Grade: {self.grade}"

class Location:
    """Location class demonstrating the use of slots.
    
    Uses __slots__ to restrict attributes and optimize memory usage.
    
    Attributes:
        name (str): Location name
        longitude (float): Geographical longitude
        latitude (float): Geographical latitude
    """
    
    __slots__ = ['name', 'longitude', 'latitude']
    
    def __init__(self, name: str, longitude: float, latitude: float):
        """Initialize a Location instance.
        
        Args:
            name: Location name
            longitude: Geographical longitude
            latitude: Geographical latitude
        """
        self.name = name
        self.longitude = longitude
        self.latitude = latitude
    
    def get_coordinates(self) -> tuple:
        """Get location coordinates as a tuple.
        
        Returns:
            tuple: (longitude, latitude)
        """
        return (self.longitude, self.latitude) 