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

class KSinfo(models.Model):
    date = models.TextField('date', max_length=36)
    status = models.TextField('status', max_length=12)
    hezhi = models.TextField('hezhi', max_length=12)
    BigS = models.TextField('BigS', max_length=24)
    SigD = models.TextField('SigD', max_length=24)

class KSinfo_ahks(models.Model):
    date = models.TextField('date', max_length=36)
    status = models.TextField('status', max_length=12)
    hezhi = models.TextField('hezhi', max_length=12)
    BigS = models.TextField('BigS', max_length=24)
    SigD = models.TextField('SigD', max_length=24)

class KSinfo_bjks(models.Model):
    date = models.TextField('date', max_length=36)
    status = models.TextField('status', max_length=12)
    hezhi = models.TextField('hezhi', max_length=12)
    BigS = models.TextField('BigS', max_length=24)
    SigD = models.TextField('SigD', max_length=24)

class KSinfo_fjks(models.Model):
    date = models.TextField('date', max_length=36)
    status = models.TextField('status', max_length=12)
    hezhi = models.TextField('hezhi', max_length=12)
    BigS = models.TextField('BigS', max_length=24)
    SigD = models.TextField('SigD', max_length=24)

class KSinfo_gsks(models.Model):
    date = models.TextField('date', max_length=36)
    status = models.TextField('status', max_length=12)
    hezhi = models.TextField('hezhi', max_length=12)
    BigS = models.TextField('BigS', max_length=24)
    SigD = models.TextField('SigD', max_length=24)

class KSinfo_gxks(models.Model):
    date = models.TextField('date', max_length=36)
    status = models.TextField('status', max_length=12)
    hezhi = models.TextField('hezhi', max_length=12)
    BigS = models.TextField('BigS', max_length=24)
    SigD = models.TextField('SigD', max_length=24)

class KSinfo_hbks(models.Model):
    date = models.TextField('date', max_length=36)
    status = models.TextField('status', max_length=12)
    hezhi = models.TextField('hezhi', max_length=12)
    BigS = models.TextField('BigS', max_length=24)
    SigD = models.TextField('SigD', max_length=24)

class KSinfo_hebks(models.Model):
    date = models.TextField('date', max_length=36)
    status = models.TextField('status', max_length=12)
    hezhi = models.TextField('hezhi', max_length=12)
    BigS = models.TextField('BigS', max_length=24)
    SigD = models.TextField('SigD', max_length=24)

class KSinfo_jsks(models.Model):
    date = models.TextField('date', max_length=36)
    status = models.TextField('status', max_length=12)
    hezhi = models.TextField('hezhi', max_length=12)
    BigS = models.TextField('BigS', max_length=24)
    SigD = models.TextField('SigD', max_length=24)

class KSinfo_jxks(models.Model):
    date = models.TextField('date', max_length=36)
    status = models.TextField('status', max_length=12)
    hezhi = models.TextField('hezhi', max_length=12)
    BigS = models.TextField('BigS', max_length=24)
    SigD = models.TextField('SigD', max_length=24)

class KSinfo_nmks(models.Model):
    date = models.TextField('date', max_length=36)
    status = models.TextField('status', max_length=12)
    hezhi = models.TextField('hezhi', max_length=12)
    BigS = models.TextField('BigS', max_length=24)
    SigD = models.TextField('SigD', max_length=24)

class KSinfo_shks(models.Model):
    date = models.TextField('date', max_length=36)
    status = models.TextField('status', max_length=12)
    hezhi = models.TextField('hezhi', max_length=12)
    BigS = models.TextField('BigS', max_length=24)
    SigD = models.TextField('SigD', max_length=24)

class KSinfo_tjks(models.Model):
    date = models.TextField('date', max_length=36)
    status = models.TextField('status', max_length=12)
    hezhi = models.TextField('hezhi', max_length=12)
    BigS = models.TextField('BigS', max_length=24)
    SigD = models.TextField('SigD', max_length=24)