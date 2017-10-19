from __future__ import unicode_literals

from django.db import models

class Books(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "Name : {},".format(self.name)

class Authors(models.Model):
    books = models.ManyToManyField(Books, related_name="authors")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)  
    notes = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)  
    def __str__(self):
        return "{} {},".format(self.first_name, self.last_name)





# Create your models here.
