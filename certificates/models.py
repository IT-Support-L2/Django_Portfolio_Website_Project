from django.db import models


class IT_Certificate(models.Model):
    # images
    image = models.ImageField(upload_to='images/')
    # summary
    summary = models.CharField(max_length=200)
    # links
    link = models.CharField(max_length=200, default="DEFAULT VALUE")

    def __str__(self):
        return self.summary
        return self.link

class DMarketing_Certificate(models.Model):
    # images
    image = models.ImageField(upload_to='images/')
    # summary
    summary = models.CharField(max_length=200)
    # links
    link = models.CharField(max_length=200, default="DEFAULT VALUE")

    def __str__(self):
        return self.summary
        return self.link

class WebDev_Certificate(models.Model):
    # images
    image = models.ImageField(upload_to='images/')
    # summary
    summary = models.CharField(max_length=200)
    # links
    link = models.CharField(max_length=200, default="DEFAULT VALUE")

    def __str__(self):
        return self.summary
        return self.link