from django import forms
from ticket_engine.models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = []
