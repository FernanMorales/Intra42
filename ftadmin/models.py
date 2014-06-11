from django.db import models

class Module(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=500)
    nb_place = models.IntegerField()
    date_insc_debut = models.DateField()
    date_insc_fin = models.DateField()
    date_mod_debut = models.DateField()
    date_mod_fin = models.DateField()
    nb_credit = models.IntegerField()

    def __unicode__(self):
        return self.name

class Activite(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=500)
    file  = models.FileField(upload_to='files/')
    sujet = models.CharField(max_length=8)
    nb_place = models.IntegerField()
    date_insc_debut = models.DateField()
    date_insc_fin = models.DateField()
    date_acti_debut = models.DateField()
    date_acti_fin = models.DateField()
    taille_groupe_min = models.IntegerField()
    taille_groupe_max = models.IntegerField()
    nb_correcteurs = models.IntegerField()
    nb_corrections = models.IntegerField()
    groupe_auto = models.BooleanField()
    module = models.ForeignKey(Module)
    TYPES = (
        ('projet', 'projet'),
        ('exam', 'exam'),
        ('TD', 'TD')
    )
    type = models.CharField(max_length=6,
                            choices=TYPES,
                            default='projet')

    def __unicode__(self):
        return self.name

class Bareme(models.Model):
    activite_associee = models.ForeignKey(Module)

    def __unicode__(self):
        return self.activite_associee