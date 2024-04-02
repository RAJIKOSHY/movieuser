from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class movie(models.Model):
    name = models.CharField(max_length=250)
    details = models.TextField()
    link = models.URLField()
    pic = models.ImageField(upload_to='gallery')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name