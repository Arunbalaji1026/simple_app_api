from django.db import models

# Create your models here.

class SimpleForm(models.Model):
    name = models.CharField(max_length=50, null = True)
    email = models.EmailField(max_length=50, null = True)
    mobile = models.IntegerField( null= True)
    address = models.CharField(max_length=250,null= True)
    city = models.CharField(max_length=50, null= True)
    state = models.CharField(max_length=50, blank= True)

    def __self__(self):
        return self.name
