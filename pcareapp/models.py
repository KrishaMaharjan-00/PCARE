from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Notification(models.Model):
    mname = models.CharField(max_length=200)
    hours = models.CharField(max_length=200)
    minutes = models.CharField(max_length=200)
    seconds = models.CharField(max_length=200)

    def __str__(self):
        return self.mname



class Pressure(models.Model):
    name = models.CharField(max_length=200)
    upperBP = models.CharField(max_length=200)
    lowerBP = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)

    def __str__(self):
        return self.name

