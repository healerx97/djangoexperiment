from django.db import models

class SampleApp(models.Model):
    title = models.TextField()
    quantity = models.IntegerField(default=1)

# Create your models here.
