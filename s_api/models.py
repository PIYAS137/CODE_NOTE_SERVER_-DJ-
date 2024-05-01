from django.db import models

# Create your models here.
class StudentAuthCredential(models.Model):
    s_id = models.IntegerField()
    s_secret = models.IntegerField()

class CodeModel(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10000)
    s_id = models.IntegerField()
    s_secret = models.IntegerField()
    date = models.CharField(max_length=40)
    course = models.CharField(max_length=40)
