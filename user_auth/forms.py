from django import forms
from django.contrib.auth.models import User


class UserLogInForm(forms.Form):
	'''
	Форма авторизации
	'''
	username = forms.CharField(label=False, widget=forms.TextInput(attrs={'class':'username', 'placeholder': 'Имя пользователя'}))
	password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'class':'password', 'placeholder': 'Пароль'}))

class UserRegisterForm(forms.ModelForm):
	'''
	Форма регистрации
	'''
	password_1 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'class':'password', 'placeholder': 'Пароль'}))
	password_2 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'class':'password', 'placeholder': 'Подтвердите пароль'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')
		labels = {
			'username': '',
			'first_name': '',
			'last_name': '',
			'email': '',
		}
		help_texts = {
			'username': '',
		}
		widgets = {
			'username': forms.TextInput(attrs={'class': 'username', 'placeholder': 'Имя пользователя'}),
			'first_name': forms.TextInput(attrs={'class': 'password', 'placeholder': 'Имя'}),
			'last_name': forms.TextInput(attrs={'class': 'password', 'placeholder': 'Фамилия'}),
			'email': forms.EmailInput(attrs={'class': 'username', 'placeholder': 'Почта'}),
		} 

	def cleaned_password2(self):
		cleaned_data = self.cleaned_data
		if cleaned_data['password_1'] != cleaned_data['password_2']:
			raise forms.ValidationError('Пароли не совпадают!')
		return cleaned_data['password_2'] 


