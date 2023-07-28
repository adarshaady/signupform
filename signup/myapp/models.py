from django.db import models

class Registration(models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=100)
    r_phone = models.CharField(max_length=15)
    r_email = models.EmailField()
    myfiles = models.ImageField(upload_to='',default='')


def __str__(self):
        return self.fname
