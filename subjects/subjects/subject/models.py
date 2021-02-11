from django.db import models


class Subject(models.Model):
    initials = models.CharField(max_length = 7, null = False, blank = False)
    name = models.CharField(max_length = 50, null = False, blank = False)
    description = models.CharField(max_length = 255, null = False, blank = False)
    ementa = models.CharField(max_length = 255, null = False, blank = False)
    created_date = models.DateField(auto_now_add = True)
    updated_date = models.DateField(auto_now_add = True)

    def __str__(self):
        return f'Sigla: {self.initials}  -  Name: {self.name}  -  Descrição: {self.description}'
