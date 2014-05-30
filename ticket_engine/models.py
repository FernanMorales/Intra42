from django.db import models
from django.utils import timezone
from django.template import RequestContext
from django.contrib.auth.models import User
# Create your models here.

class Type(models.Model):
	problem_type = models.CharField(max_length=200)

	def __unicode__(self):
		return self.problem_type

class Ticket(models.Model):
	PRIORITIES = (
    (0, 'Low'),
    (1, 'Normal'),
    (2, 'High'),
    )
	title = models.CharField(max_length=30)
	content = models.TextField()
	priority = models.IntegerField(default=0, choices=PRIORITIES)
	status = models.IntegerField(default=0)
	queue = models.ForeignKey(Type)
	user = models.CharField(max_length=8)
	pub_date = models.DateTimeField('date published', default=timezone.now)

	def __unicode__(self):
		return self.title