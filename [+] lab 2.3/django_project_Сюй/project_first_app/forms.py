from django import forms
from .models import Owner, User

class OwnerForm(forms.ModelForm):
    username = forms.CharField(max_length=150, label="Имя пользователя")
    passport_number = forms.CharField(max_length=10, label="Номер паспорта")
    home_address = forms.CharField(max_length=255, label="Домашний адрес")
    nationality = forms.CharField(max_length=50, label="Национальность")

    class Meta:
        model = Owner
        fields = ['birth_date']  # Поля модели Owner

    def save(self, commit=True):
        owner = super().save(commit=False)
        user_data = {
            'username': self.cleaned_data['username'],
            'passport_number': self.cleaned_data['passport_number'],
            'home_address': self.cleaned_data['home_address'],
            'nationality': self.cleaned_data['nationality']
        }

        if commit:
            # Создаём пользователя
            user = User.objects.create(**user_data)
            owner.user = user
            owner.save()

        return owner

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'passport_number', 'home_address', 'nationality', 'first_name', 'last_name']

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'passport_number', 'home_address', 'nationality']
        widgets = {
            'password': forms.PasswordInput(),
        }
