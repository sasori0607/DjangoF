from django import forms


class UserForm(forms.Form):
     first_name= forms.CharField(max_length=100, label='Ваше Имя')
     email= forms.EmailField(label='Почта')
     text = forms.CharField(label='Ваш Вопрос',widget=forms.Textarea(attrs={'rows':4, 'cols':23}))