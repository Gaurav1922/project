from django.db import models

# Create your models here.
class Record(models.Model):
    emp_id = models.IntegerField(unique=True, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    department = models.CharField(max_length=50, default='Unknown')
    designation = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=300)


    def __str__(self):
        return self.name





