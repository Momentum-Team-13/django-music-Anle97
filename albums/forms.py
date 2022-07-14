from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'artist', 'date', 'songcount',]
        labels = {
            'title': 'Title',
            'artist': 'Artist',
            'date': 'Album Release Date',
            'songcount': 'Album Song Count',
        }