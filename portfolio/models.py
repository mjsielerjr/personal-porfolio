from django.db import models
from django.conf import settings
import os

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/', blank=True)
    url = models.URLField(blank=True)  # "blank=True" means having a url is optional
    file = models.FileField(upload_to='portfolio/files/', blank=True)

    def __str__(self):
        return self.title
