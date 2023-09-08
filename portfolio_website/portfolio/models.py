from django.db import models
from datetime import datetime

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to="images/")
    description = models.TextField(blank=True)
    technology = models.CharField(max_length=50)
    date_publish = models.DateTimeField(default=datetime.now, blank=True)
