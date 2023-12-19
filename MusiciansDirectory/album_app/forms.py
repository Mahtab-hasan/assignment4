from django import forms
from .models import Album
from musician_app.models import Musician

class AlbumForm(forms.ModelForm):
    musician = forms.ModelChoiceField(queryset=Musician.objects.all(), required=True)
    class Meta:
        model = Album
        fields = ['album_name', 'musician','release_date','rating']
        