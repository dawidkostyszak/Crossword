from django import forms
from models import Difficulty


class WordForm(forms.Form):
    name = forms.CharField()
    question = forms.CharField(widget=forms.Textarea)
    difficulty = forms.ModelChoiceField(
        queryset=Difficulty.objects.all()
    )