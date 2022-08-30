from django import forms


class CreatePostForm(forms.Form):
	'''
	Форма создания поста
	'''
	post_text = forms.CharField(label=False, widget=forms.Textarea(attrs={
		'class': 'textarea',
		'placeholder': 'Опубликуйте запись',
	}))


class ProfileEditForm(forms.Form):
	'''
	Форма редактирования профиля
	'''
	name = forms.CharField(required=False, label=False, widget=forms.TextInput(attrs={
		'class': 'username',
		'placeholder': 'Имя',
	}))
	surname = forms.CharField(required=False, label=False, widget=forms.TextInput(attrs={
		'class': 'username surname',
		'placeholder': 'Фамилия',
	}))
	age = forms.CharField(required=False, label=False, widget=forms.TextInput(attrs={
		'class': 'num',
		'placeholder': 'Возраст',
		'type': 'number',
		'min':'0',
		'max': '100',
	}))
	work_exp = forms.CharField(required=False, label=False, widget=forms.TextInput(attrs={
		'class': 'num',
		'placeholder': 'Опыт',
		'type': 'number',
		'min':'0',
		'max': '30',
	}))
	location = forms.CharField(required=False, label=False, widget=forms.TextInput(attrs={
		'class': 'username',
		'placeholder': 'Локация',
		'list': 'location',
	}))
	it_stack = forms.CharField(required=False, label=False, widget=forms.TextInput(attrs={
		'class': 'username',
		'placeholder': 'Направление в IT',
		'list': 'stack',
	}))
	avatar = forms.ImageField(required=False, label='Аватар: ', widget=forms.FileInput())
	