from django.contrib import admin
from ticket_engine.models import Ticket, Type

# Register your models here.

admin.site.register(Ticket)
admin.site.register(Type)