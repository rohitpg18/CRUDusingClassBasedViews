from django.db import models

class Student(models.Model):
    id = models.IntegerField(primary_key=True , null=False)
    name = models.CharField(max_length=255 , null=True)
    phone_number = models.CharField(max_length=10 , null=True)
    email = models.EmailField(default=None, null=True)

    def __str__(self):
        return self.name
    
    
    
    #('id', 'name', 'phone_number', 'email', )