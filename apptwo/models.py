from django.db import models

class SampleApp(models.Model):
    title = models.TextField()
    quantity = models.IntegerField(default=1)
    extra = models.BooleanField(null = True)
# Create your models here.
