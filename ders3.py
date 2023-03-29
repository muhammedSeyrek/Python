#OOP
#%%
#OOP'nin temel ilkesi
#1)Kapsulleme(Encapsulation), Soyutlama(Abstraction)
#2)Kalitim (Inheritance)
#3)Cok - Sekililik(Polymorphism)

#Sinif : [Data (data members - veri uyeleri); Functions - Uye fonksiyonlar]
#Sinif Bilgisayar(cpu, hdd, ram, graphicsCard Functions : Uyumlu(), Goruntule())

class Student:
    def __init__(self, name, studentNumber):
        self.name = name
        self.studentNumber = studentNumber
        self.classes = []

    def enrol(self, courseRun):
        self.classes.append(courseRun)
        courseRun.addStudent(self)

class Department:
    def __init__(self, name, departmentCode):
        self.name = name
        self.departmentCode = departmentCode
        self.courses = {}

    def addCourse(self, destcription, courseCode, credits):
        self.courses[courseCode] 

class Course:
    def __init__(self):
        self


class CourseRunning:
    def __init__(self, course, year):
        self.course = course
        self.year = year






#%%Ornek
import math

class Sekil:
    def alan(self):
        raise NotImplementedError()
#Inheritance + Encapsulation

class Kare(Sekil):
    def __init__(self, genislik):
        self.genislik = genislik
    
    def alan(self):
        return self.genislik ** 2

class Daire(Sekil):
    def __init__(self, yaricap):
        self.yaricap = yaricap

    def alan(self):
        return math.pi * self.yaricap ** 2 

sekiller = [Kare(2), Daire(4)]

#Polymorphism

print([oge.alan() for oge in sekiller])























































 
# %%
