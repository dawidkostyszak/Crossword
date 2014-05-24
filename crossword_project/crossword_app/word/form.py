from django import forms


class WordForm(forms.Form):
    name = forms.CharField()
    question = forms.CharField(widget=forms.Textarea)
    category = forms.ChoiceField(required=False, choices=[('sport', 'Sport'), ('ogolne', 'Ogolne')], initial='ogolne')