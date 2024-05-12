# zadanie 1

from math import pi

class Shape:
    def __init__(self, area,):
        pass
    def __init__(self, perimeter):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, base, height, side1, side2):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.base + self.side1 + self.side2

circle = Circle(5)
print("Area of Circle is: ", circle.area())
print("Perimeter of Circle is: ",circle.perimeter())

rectangle = Rectangle(9, 10)
print("Area of Rectangle is: ",rectangle.area())
print("Perimeter of Rectangle is: ",rectangle.perimeter())

triangle = Triangle(5, 10, 5, 5)
print("Area of Triangle is: ",triangle.area())
print("Perimeter of Triangle is: ",triangle.perimeter())

# zadanie 2

import datetime

class Task:
    def __init__(self, description, priority, due_date):
        self.description = description
        self.priority = priority
        self.due_date = due_date

    def __str__(self):
        return f"Task: {self.description}, Priority: {self.priority}, Due date: {self.due_date}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority, due_date):
        task = Task(description, priority, due_date)
        self.tasks.append(task)

    def remove_task(self, description):
        self.tasks = [task for task in self.tasks if task.description != description]

    def view_tasks(self):
        for task in self.tasks:
            print(task)

task_manager = TaskManager()
task_manager.add_task("Finish project", "High", datetime.date(2023, 5, 17))
task_manager.add_task("Buy steel", "Low", datetime.date(2023, 5, 10))
task_manager.view_tasks()
task_manager.remove_task("Finish project")
task_manager.view_tasks()

#zadanie 3
# zadanie przesle w tygodniu
