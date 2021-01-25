from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=80, required=False)
    email = forms.EmailField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2')
        help_texts = {
            'username': None,
            'name': 'optional.',
            'email': 'required with confirmation email',
        }