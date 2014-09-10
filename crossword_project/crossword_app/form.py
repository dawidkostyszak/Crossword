from django import forms
from word.models import Difficulty


class CrosswordForm(forms.Form):
    word = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Put main word'})
    )
    difficulty = forms.ModelChoiceField(
        queryset=Difficulty.objects.all()
    )