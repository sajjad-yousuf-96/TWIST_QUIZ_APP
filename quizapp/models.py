from django.db import models

# Create your models here.
class QuizCode(models.Model):
    userid=models.CharField(max_length=200,null=True)
    quizcode=models.CharField(max_length=200,null=True)
    
class QuizData(models.Model):
    question=models.CharField(max_length=200,null=True)
    wrongansw1=models.CharField(max_length=200,null=True)
    wrongansw2=models.CharField(max_length=200,null=True)
    wrongansw3=models.CharField(max_length=200,null=True)
    wrongansw4=models.CharField(max_length=200,null=True)
    correctansw=models.CharField(max_length=200,null=True)
    qquizcode=models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question
        
class StudentData(models.Model):
    name=models.CharField(max_length=200,null=True)
    rollno=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    confirmpassword=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class MCQAttemptStudent(models.Model):
    name=models.CharField(max_length=200,null=True)
    rollno=models.CharField(max_length=200,null=True)
    quizcode=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name


class StudentMarks(models.Model):
    rollno=models.CharField(max_length=200,null=True)
    quizcode=models.CharField(max_length=200,null=True)
    marks=models.CharField(max_length=200,null=True)

