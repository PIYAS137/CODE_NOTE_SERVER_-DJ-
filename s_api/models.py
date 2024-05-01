from django.db import models

# Create your models here.
class StudentAuthCredential(models.Model):
    s_id = models.IntegerField()
    s_secret = models.IntegerField()