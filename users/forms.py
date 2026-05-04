from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import get_user_model,authenticate


User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
	username = forms.CharField(required=True,max_length=128,
	                           widget=forms.TextInput(attrs={'class':'input-register form-control','placeholder':'Your username'}))
	first_name = forms.CharField(required=True, max_length=50,
	                             widget=forms.TextInput(attrs={'class':'input-register form-control','placeholder':'Your first name'}))
	last_name = forms.CharField(required=True, max_length=50,
	                             widget=forms.TextInput(attrs={'class':'input-register form-control','placeholder':'Your last name'}))
	password1 = forms.CharField(required=True,
	                            widget=forms.PasswordInput(attrs={'class':'input-register form-control','placeholder':'Your password'}))
	password2 = forms.CharField(required=True,
	                            widget=forms.PasswordInput(attrs={'class':'input-register form-control','placeholder':'Confirm your password'}))

	class Meta:
		model = User
		fields = ('username','first_name','last_name','password1','password2')

		def clean_username(self):
			username = self.cleaned_data.get('username')
			if User.objects.filter(username=username).exists():
				raise forms.ValidationError('This username is already in use')
			return username

		def save(self,commit=True):
			user = super().save(commit = False)
			if commit:
				user.save()
			return user

