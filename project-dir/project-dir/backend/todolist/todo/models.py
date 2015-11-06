from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class List(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

class Todo(models.Model):
    list = models.ForeignKey(List)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    done = models.BooleanField(default=False)

    def __unicode__(self):
        return "" + self.list.title + "'s " + self.name

class Permissions(models.Model):
    list = models.OneToOneField(List)
