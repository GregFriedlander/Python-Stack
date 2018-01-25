from __future__ import unicode_literals
import bcrypt
import re
from django.db import models
from datetime import date

# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UsersManager(models.Manager):
    def validate_reg(self, post_data):
        errors = {}
        if len(post_data['name']) < 3:
            errors['name'] = "Name must be at least 3 characters"
        if len(post_data['username']) < 3:
            errors['username'] = "Username must be at least 3 characters"
        if not re.match(EMAIL_REGEX, post_data['email']):
            errors['email'] = "Please enter a valid Email"
        if len(post_data['password']) < 8:
            errors['password'] = "Password must be at least 8 characters long"
        if post_data['password'] != post_data['password_confirm']:
            errors['password_conf'] = "Please confirm your password correctly"
        if Users.objects.filter(email=post_data['email']):
            errors['email_exists'] = "Sorry but that email address is already in use"
        return errors

    def validate_login(self, post_data):
        user_to_check = Users.objects.get(email=post_data['email'])
        if user_to_check:
            if bcrypt.checkpw(post_data['password'].encode(), user_to_check.password.encode()):
                user = {
                    "user": user_to_check
                }
                return user
            else:
                errors = {
                    "error": "Login Invalid"
                }
                return errors
        else:
            errors = {
                "error": "Login Invalid"
            }
            return errors

class Users(models.Model):




