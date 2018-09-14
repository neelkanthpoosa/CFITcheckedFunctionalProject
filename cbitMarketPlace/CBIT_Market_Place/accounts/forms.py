from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from phonenumber_field.modelfields import PhoneNumberField
from .models import UserProfile

class RegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True,widget=forms.EmailInput(
	attrs={
	'class':'form__input',
	'placeholder':'Email',
	}
	))
    username=forms.CharField(required=True,widget=forms.TextInput(
	attrs={
	'class':'form__input',
	'placeholder':'Username',
	}
	))
    password1=forms.CharField(required=True,widget=forms.PasswordInput(
	attrs={
	'class':'form__input',
	'placeholder':'Password',
	}
	))
    password2=forms.CharField(required=True,widget=forms.PasswordInput(
	attrs={
	'class':'form__input',
	'placeholder':'Confirm Password',
	}
	))
    first_name=forms.CharField(required=True,widget=forms.TextInput(
	attrs={
	'class':'form__input',
	'placeholder':'First Name',
	}
	))
    last_name=forms.CharField(required=True,widget=forms.TextInput(
	attrs={
	'class':'form__input',
	'placeholder':'Last Name',
	}
	))

    
    class Meta:
        model = User
        fields = ('username',
                'first_name',
                'last_name',
                'email',
                'password1',
                'password2',
                )

    def save(self,commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
            )


class ProfileForm(forms.ModelForm):
    description = forms.CharField(required=True)

    class Meta:
        model = UserProfile
        fields = (
        'description',
        'phone',
        'image',
        )
