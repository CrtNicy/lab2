from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Owner, Car, Ownership, DriverLicense, User


class CustomUserAdmin(UserAdmin):
    # Добавляем новые поля в административный интерфейс
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительная информация', {
            'fields': ('passport_number', 'home_address', 'nationality'),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Дополнительная информация', {
            'fields': ('passport_number', 'home_address', 'nationality'),
        }),
    )

    # Отображение новых полей в списке пользователей
    list_display = UserAdmin.list_display + ('passport_number', 'home_address', 'nationality')


# Регистрируем кастомную модель пользователя
admin.site.register(User, CustomUserAdmin)


class OwnerAdminForm(forms.ModelForm):
    # Поля из модели User
    passport_number = forms.CharField(
        max_length=10,
        label="Номер паспорта",
        required=False
    )
    home_address = forms.CharField(
        max_length=255,
        label="Домашний адрес",
        required=False
    )
    nationality = forms.CharField(
        max_length=50,
        label="Национальность",
        required=False
    )

    class Meta:
        model = Owner
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['passport_number'].initial = self.instance.user.passport_number
            self.fields['home_address'].initial = self.instance.user.home_address
            self.fields['nationality'].initial = self.instance.user.nationality


class OwnerAdmin(admin.ModelAdmin):
    form = OwnerAdminForm
    list_display = ('user', 'birth_date')

    def save_model(self, request, obj, form, change):
        # Сохраняем дополнительные поля в связанную модель User
        user = obj.user
        if 'passport_number' in form.cleaned_data:
            user.passport_number = form.cleaned_data['passport_number']
        if 'home_address' in form.cleaned_data:
            user.home_address = form.cleaned_data['home_address']
        if 'nationality' in form.cleaned_data:
            user.nationality = form.cleaned_data['nationality']
        user.save()
        super().save_model(request, obj, form, change)


# Регистрируем кастомного владельца
admin.site.register(Owner, OwnerAdmin)

# Остальные модели
admin.site.register(Car)
admin.site.register(Ownership)
admin.site.register(DriverLicense)
