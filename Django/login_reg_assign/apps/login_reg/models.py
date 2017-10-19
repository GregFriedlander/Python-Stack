from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

class UsersManager(models.Manager):
    def validate_reg(self, post_data):
        errors = {}
        if len(post_data['first_name']) < 2 or len(post_data['last_name']) < 2:
            errors['name'] = "first name/last name must be at least 2 characters"
        if (post_data['first_name'].isalpha() == False and len(post_data['first_name']) > 0) or (post_data['last_name'].isalpha() == False and len(post_data['last_name']) > 0):
            errors['name_nonum'] = "first name/last name must only contain letters"
        if len(post_data['email']) < 1:
            errors['email_len'] = "please enter an email"
        if not re.match(EMAIL_REGEX, post_data['email']) and len(post_data['email']) > 0:
            errors['email'] = "not a valid email"
        if len(post_data['password']) < 8 or len(post_data['password_confirm']) < 8:
            errors['pass_length'] = "please enter a password at least 8 characters long and confirm it correctly"
        if post_data['password'] != post_data['password_confirm']:
            errors['password_conf'] = "please confirm the correct password"   
        if Users.objects.filter(email=post_data['email']):
            errors['exists'] = "That email is already in use"     
        return errors
    
    def login_reg(self, post_data):
        user_to_check = Users.objects.get(email=post_data['email'])
        # print user_to_check
        if user_to_check:
            # user_to_check = user_to_check[0]
            if bcrypt.checkpw(post_data['password'].encode(), user_to_check.password.encode()):
                user = {
                    "user": user_to_check
                }
                return user
            else:
                # print "past user to check failed password check"
                errors = {
                    "error": "Login Invalid"
                }
                return errors
        else:
            # print "failed user to check"
            errors = {
                    "error": "Login Invalid"
                }
            return errors
            

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UsersManager()