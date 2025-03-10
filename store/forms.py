from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):

    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))

    last_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')



    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'User Name'
        })
        self.fields['username'].label = ''
        self.fields['username'].help_text = ()

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ()

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        })
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = ()
