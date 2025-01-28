from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Owner(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    birth_date = models.DateField(null=True, verbose_name="Дата рождения")

    def __str__(self):
        return self.user.username


# Модель "Автомобиль"
class Car(models.Model):
    license_plate = models.CharField(max_length=15, verbose_name="Номерной знак")
    brand = models.CharField(max_length=20, verbose_name="Марка")
    model = models.CharField(max_length=20, verbose_name="Модель")
    color = models.CharField(max_length=30, verbose_name="Цвет")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.license_plate})"


class Ownership(models.Model):
    owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE,
        related_name="ownership_set",
        verbose_name="Владелец"
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        verbose_name="Автомобиль"
    )
    start_date = models.DateField(verbose_name="Дата начала владения")
    end_date = models.DateField(null=True, blank=True, verbose_name="Дата окончания владения")

    def __str__(self):
        return f"{self.owner} владеет {self.car}"



# Модель "Водительское удостоверение"
class DriverLicense(models.Model):
    owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE,
        verbose_name="Владелец"
    )
    license_number = models.CharField(max_length=10, verbose_name="Номер удостоверения")
    license_type = models.CharField(max_length=10, verbose_name="Тип удостоверения")
    issue_date = models.DateField(verbose_name="Дата выдачи")

    def __str__(self):
        return f"{self.license_number} ({self.owner})"


# Кастомная модель пользователя
class User(AbstractUser):
    passport_number = models.CharField(max_length=10, blank=True, null=True, verbose_name="Номер паспорта")
    home_address = models.CharField(max_length=255, blank=True, null=True, verbose_name="Домашний адрес")
    nationality = models.CharField(max_length=50, blank=True, null=True, verbose_name="Национальность")

    def __str__(self):
        return self.username
