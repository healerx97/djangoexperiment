from django.db import models

class SampleApp(models.Model):
    title = models.TextField()
    quantity = models.IntegerField(default=1)
    extra = models.BooleanField(null = True)

class SampleModelTwo(models.Model):
    name = models.TextField()

class Feed(models.Model):
    title = models.TextField()
    author = models.TextField()


class Publisher(models.Model):
    feeds = models.ManyToManyField(feed, on_delete=models.CASCADE)
    
# Create your models here.
