from django import forms
from crossword_project.crossword_app.word.models import Category


class WordForm(forms.Form):
    name = forms.CharField()
    question = forms.CharField(widget=forms.Textarea)
    category = forms.ModelChoiceField(required=False, queryset=Category.objects.all(), initial=1)