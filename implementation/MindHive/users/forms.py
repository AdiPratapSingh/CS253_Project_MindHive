import sys

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from tags.models import Tag
from .models import User


sys.path.append("..")


# form for signing up
class UserCreateForm(UserCreationForm):
    class Meta:
        # declare the approproate fields
        fields = ('username', 'name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address'}),
        }
        model = get_user_model()

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = ''
        self.fields['username'].label = ''
        self.fields['name'].label = ''


# form for editing the username and the profile image
class UpdateUserInfo(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","profile_image"]
        widgets={
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your new user name'}),
        }
        profile_image=forms.ImageField()


# form for adding the favourite tags
class addTagsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['favouriteTags']
        labels = {'favouriteTags': 'Favourite Tags'}
        widgets = {
            'favouriteTags': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input form-check-inline',
                }),
        }
        # favouriteTags = forms.ModelMultipleChoiceField(
        #                 queryset=Tag.objects.all(),
        #                 widget=forms.CheckboxSelectMultiple)