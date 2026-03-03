from django import forms
from .models import Announcement, PhotoAnnouncement
from django.forms import inlineformset_factory

class AnnouncementForms(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['main_photo', 'title', 'city', 'price', 'phone', 'state', 'state_components', 'manufacture', 'guarantee', 'complete','description']

PhotoFormSet = inlineformset_factory(Announcement, PhotoAnnouncement, fields = ('photo',), extra=5)