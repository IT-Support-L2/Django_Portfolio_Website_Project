from django.db import models

# Create your models here.

class Project(models.Model):
    # images
    image = models.ImageField(upload_to='images/')
    # summary
    summary = models.CharField(max_length=200)
    # links
    link = models.CharField(max_length=200, default="DEFAULT VALUE")

    def __str__(self):
        return self.summary
        return self.link