from django.db import models

# Create your models here.
class Employee(models.Model):

    name = models.CharField(max_length=80)
    position_at_work = models.CharField(max_length=80)

class PersonalData(models.Model):
    phone = models.CharField(max_length=40)
    Email = models.EmailField()
    address = models.CharField(max_length=80)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="employees", related_query_name='employee')