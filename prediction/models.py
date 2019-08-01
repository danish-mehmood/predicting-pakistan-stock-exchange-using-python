from django.db import models

# Create your models here.



class News(models.Model):

     headline = models.CharField(max_length = 300)
     url  = models.URLField(max_length  = 300)
     image  = models.ImageField(null=True )
     date = models.DateField()

     def __str__(self):
         return self.headline
