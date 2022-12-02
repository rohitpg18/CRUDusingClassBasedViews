from django.db import models

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    # design = models.CharField(max_length=50 , choices=p_choices, null=True)
    name = models.CharField(max_length=255)
    # spend_time = models.DateTimeField(null=True)
    # text = models.TextField(null=True)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(default=None)
    # image = models.ImageField(upload_to='api' , height_field=10 , width_field=20 , max_length=100, default=None, blank=True)

    def __str__(self):
        return self.name