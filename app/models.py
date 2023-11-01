from django.db import models



class arch(models.Model):
    
    # files = models.FileField(upload_to='documents/')
    files = models.FileField()
    
    # images=models.ImageField(upload_to='images/')

    