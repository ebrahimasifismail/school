from django.db import models

class Classes(models.Model):
    standard = models.CharField(max_length=250)
    division = models.CharField(max_length=25)
 
    def __str__(self):
        return self.standard

class Subject(models.Model):
    name = models.CharField(max_length=200)
    standard = models.ForeignKey(Classes, related_name="student_class", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class OptionalSubject(models.Model):
    name = models.CharField(max_length=200)
    standard = models.ForeignKey(Classes, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=250)
    standard = models.ForeignKey(Classes, related_name="student_classes", on_delete=models.CASCADE)
    division = models.CharField(max_length=25)
    subject = models.ForeignKey(Subject, related_name="subject", null=True, on_delete=models.CASCADE)
    optn_subject = models.ForeignKey(OptionalSubject, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name 
