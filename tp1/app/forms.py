from django import forms
from .models import Cours

class CourForm(forms.ModelForm):

    class Meta:
        model = Cours
        fields = ('title', 'former', 'hours', 'first_lesson')

class NoteForm(forms.ModelForm):
    class Meta:
        model =  Cours
        fields = ('note',)
