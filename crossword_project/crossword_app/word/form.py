from django import forms
from models import Category


class WordForm(forms.Form):
    name = forms.CharField()
    question = forms.CharField(widget=forms.Textarea)
    category = forms.ModelChoiceField(required=False, queryset=Category.objects.all(), initial=1)