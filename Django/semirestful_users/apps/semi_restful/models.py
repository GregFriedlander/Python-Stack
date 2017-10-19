from __future__ import unicode_literals
import re
from django.db import models

# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UsersManager(models.Manager):
    def validate(self, post_data):
        errors = {}

        # check all fields for emptyness
        for field, values in post_data.iteritems():
            if len(values) < 1: 
                errors[field] = "{} field is required".format(field.replace('_',' '))
            
            # check name fields for min length
            if field == "first_name" or field == "last_name":
                if not field in errors and len(values) < 3:
                    errors[field] = "{} field must be at least 3 characters".format(field.replace('_',' '))

        # check email field for valid email
        if not 'email' in errors and not re.match(EMAIL_REGEX, post_data['email']):
            errors['email'] = "invalid email"
        
        # if email is valid check db for existing email 
        else:
            if len(self.filter(email=post_data['email'])) > 1:
                errors['email'] = "email already in use"
        
        return errors



class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UsersManager()
    def __str__(self):
        return self.email