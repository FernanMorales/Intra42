from django.db import models


class Student(models.Model):
    login = models.CharField(max_length=8)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    photo = models.TextField()
    '''

    *************************************************
    *                                               *
    *   A DECOMMENTER QUAND AVANT LE DERNIER PUSH   *
    *                                               *
    *************************************************

    is_staff = models.BooleanField(u'staff status', default=False,
                help_text=u'Designates whether the user can log into this admin '
                    'site.')
    is_superuser = models.BooleanField(u'active', default=True,
                help_text=u'Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.')

    is_active = models.BooleanField(u'active', default=True,
                help_text=u'Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.')
    '''
    def __unicode__(self):
        return self.login