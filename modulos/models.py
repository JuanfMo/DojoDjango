from django.db import models
from django.utils import timezone

# Create your models here.


class facultad(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default= timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class programa(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    faculty = models.ForeignKey(facultad)
    created_date = models.DateTimeField(default= timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
