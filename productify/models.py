from django.db import models

# Create your models here.

#Employee Model <Data>
class Employee(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    emplyee_id = models.IntegerField()

    #String Represnetation 
    def __str__(self):
        return f"{self.first_name} {self.last_name}"



