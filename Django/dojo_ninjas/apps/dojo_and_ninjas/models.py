from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Dojos(models.Model):
    name = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 255)
    desc = models.TextField()
    def __str__(self):
        return "{},{}, {}, {}".format(self.name, self.city, self.state, self.desc)

class Ninjas(models.Model):
    dojo = models.ForeignKey(Dojos, related_name="ninjas")
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)

