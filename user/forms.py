from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model,authenticate


User = get_user_model()


class RegisterationForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'id': 'username'}
    ))
    email = forms.EmailField(max_length=150, widget=forms.EmailInput(
        attrs={'id': 'email'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'id': 'password'}
    ))
    avatar = forms.FileField(widget=forms.FileInput())

    def clean(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(_('User already exists.'))
        else:
            return self.cleaned_data

    def save(self):
        return User.objects.create_user(**self.cleaned_data)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'id': 'username'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'id': 'password'}
    ))

    def clean(self):
        user = authenticate(**self.cleaned_data)
        if user is None:
            raise forms.ValidationError('Cant login with given credentials')
        self.cleaned_data['user'] = user
        return self.cleaned_data
