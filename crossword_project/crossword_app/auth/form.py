from django import forms


class BasicForm(forms.Form):
    error_css_class = 'has_error'
    required_css_class = 'required'


class LoginForm(BasicForm):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistryForm(BasicForm):
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()

    def clean(self):
        password = self.cleaned_data.get('password')
        repeat_password = self.cleaned_data.get('repeat_password')

        if password and password != repeat_password:
            raise forms.ValidationError("Passwords don't match")

        return self.cleaned_data
