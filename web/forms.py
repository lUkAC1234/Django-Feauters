from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from .models import UserModel, BlogModel
from django.utils.translation import gettext_lazy as _
from ckeditor.widgets import CKEditorWidget
from django.forms.widgets import ClearableFileInput


# --------------------------------------------------------------------------- #
# User Model Form
class AccountForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['first_name','user_image', 'company', 'location', 'email', 'position', 'mobileNumber', 'socialMedia']

class BlogModelForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    class Meta: 
        model = BlogModel
        exclude = ('created_at', 'updated_at')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=16, widget=forms.TextInput(attrs={
        'placeholder': _('Enter your username')
    }))

    password = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={
        'placeholder': _('Enter you password')
    }))

    class Meta:
        model = UserModel
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_confirm_password(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if user == None:
            raise ValidationError(_('Username or password is incorrect'))
        return cleaned_data

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_confirm_password(self):
        if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise ValidationError('Passwords do not same')
        return self.cleaned_data['confirm_password']

    def clean_username(self):
        try:
            user = UserModel.objects.get(username=self.cleaned_data['username'])
            if user:
                raise ValidationError('This username is already in use')
        except:
            return self.cleaned_data['username']
        