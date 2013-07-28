#coding:utf8
from django.db import models
from django.contrib.auth.models import User
from blog.forms import UrlForm
import hashlib
class Url(models.Model):
    long_url  = models.CharField(max_length=300)
    short_url = models.CharField(max_length=20)
    def __unicode__(self):
        return self.long_url
class User(models.Model):
    user=models.OneToOneField(User)
    sex=models.CharField(max_length=2,choices=(('f','女'),('m','男')))
    birthday=models.DateField()
    def __unicode__(self):
        return self.user.username

