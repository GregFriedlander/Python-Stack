from __future__ import unicode_literals
import re
from django.db import models

# Create your models here.

class CoursesManager(models.Manager):
    def validate(self, post_data):
        errors = {}

        for field, values in post_data.iteritems():
            if len(values) < 1:
                errors[field] = "{} field is required".format(field)
            
            if field == "name":
                if not field in errors and len(values) < 5:
                    errors[field] = "{} field must be at least 5 characters".format(field)
            
            if field == "description":
                if not field in errors and len(values) < 15:
                    errors[field] = "{} field must be at least 15 characters".format(field)
        
        return errors

class Courses(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = CoursesManager()