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
    
    def clean_note(self):
        note = self.cleaned_data['note']
        if note < 0 or note > 20:
            raise forms.ValidationError("La note doit être comprise entre 0 et 20.")
        return note
