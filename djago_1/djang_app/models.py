from django.db import models

# Create your models here.
class school(models.Model):
    name =  models.CharField(max_length=20)
    age = models.CharField(max_length=2)
    place = models.CharField(max_length=25)
    email = models.EmailField()
    class_no = models.IntegerField()
    phone = models.CharField(max_length=10)
    photos = models.ImageField( upload_to='media/') 



    def __str__(self):
        return self.name
    

    
