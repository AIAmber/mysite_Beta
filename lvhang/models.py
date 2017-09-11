from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)

class Message(models.Model):
    user = models.CharField('name', max_length=32)
    mail = models.EmailField('Email', max_length=32)
    message = models.TextField('content', max_length=255)
    date = models.DateTimeField('Created Time', auto_now_add=True)