from django.db import models
from subjects.subject.models import Subject
 

class Course(models.Model):
    name = models.CharField(max_length = 50, null = False, blank = False)
    description = models.CharField(max_length = 255, null = False, blank = False)
    created_date = models.DateField(auto_now_add = True)
    update_date = models.DateField(auto_now_add = True)
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return f'Name: {self.name}  -  Descrição: {self.description}'
