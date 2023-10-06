from django.db import models

# Create your models here.
class emp(models.Model):
    Name=models.CharField(max_length=200)
    email=models.EmailField(max_length=50)
    phone=models.IntegerField(max_length=10)
    adderess=models.TextField(max_length=50)

    def __str__(self):
        return self.Name    #SHOW NAME IN ADMIN PANNEL
    