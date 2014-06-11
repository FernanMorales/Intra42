from django.db import models


class Student(models.Model):
    login = models.CharField(max_length=8)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    is_staff = models.BooleanField()

    def __unicode__(self):
        return self.login
