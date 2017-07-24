from django.db import models
import datetime

class Contact(models.Model):
    FirstName = models.CharField( max_length=50, null=True)
    LastName = models.CharField( max_length=50)
    Email =  models.EmailField(max_length=50)
    MobileNo = models.DecimalField(max_digits=12, decimal_places=0)
    #LastModifiedDate = models.DateTimeField(default=datetime.datetime.now)


    def __str__(self):
       return self.LastName + self.FirstName
