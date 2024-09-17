
from django.db import models


class Group(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"

class Subject(models.Model):
    name = models.CharField(max_length=20)
    group= models.ForeignKey(Group,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name,self.group}"

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    group=models.CharField(max_length=2)

    def __str__(self):
        return f"{self.first_name,self.last_name,self.email,self.group}"


class Exam(models.Model):
    name = models.TextField

    def __str__(self):
        return f"{self.name}"



class Question(models.Model):
    name= models.CharField(max_length=200)
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name,self.exam}"


class StudentExam(models.Model):
    exam = models.OneToOneField(Exam,on_delete=models.SET_NULL,null=True)
    student =models.ForeignKey(Student,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.exam,self.student}"

class Isoption(models.Model):
    name = models.TextField
    question = models.BooleanField(Question,default=False)





