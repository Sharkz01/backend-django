from django.db import models
from datetime import datetime

# Create your models here.
class PostJob(models.Model):
    title = models.CharField(max_length=120)
    image = models.TextField()
    company = models.CharField("Company Name", max_length=120)
    link = models.CharField(max_length=400)
    post = models.CharField(max_length=400, default=str(datetime.today().strftime('%Y-%m-%d')))
    description = models.TextField()
    agency = models.BooleanField(default=False)

    def __str__(self):
        return self.title
