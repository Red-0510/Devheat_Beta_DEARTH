from django import forms
from event.models import Event
from tinymce.widgets import TinyMCE
class AddEventForm(forms.ModelForm):
    content=forms.CharField(widget=TinyMCE(attrs={'cols':80,'rows':17}))
    class Meta:
        model=Event
        fields='__all__'