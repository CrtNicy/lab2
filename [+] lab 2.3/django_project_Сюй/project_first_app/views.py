from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic import ListView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Owner, Car
from .forms import OwnerForm, CustomUserCreationForm

def home(request):
    return render(request, 'home.html')

def owner_detail(request, owner_id):
    """
    Отображение детальной информации о владельце автомобиля.
    """
    owner = get_object_or_404(Owner, pk=owner_id)
    return render(request, 'owner_detail.html', {'owner': owner})

def owner_list(request):
    owners = Owner.objects.all()  # Получаем всех владельцев
    return render(request, 'owner_list.html', {'owners': owners})

def owner_create(request):
    if request.method == "POST":
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('owner_list')  # Перенаправление на список владельцев
    else:
        form = OwnerForm()
    return render(request, 'owner_form.html', {'form': form})

def owner_update(request, pk):
    owner = get_object_or_404(Owner, pk=pk)
    if request.method == "POST":
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owner_list')
    else:
        form = OwnerForm(instance=owner)
    return render(request, 'owner_form.html', {'form': form})

def owner_delete(request, pk):
    owner = get_object_or_404(Owner, pk=pk)
    if request.method == "POST":
        owner.delete()
        return redirect('owner_list')
    return render(request, 'owner_confirm_delete.html', {'owner': owner})

class CarListView(ListView):
    model = Car  # Указываем модель для списка
    template_name = 'car_list.html'  # Указываем имя шаблона
    context_object_name = 'cars'  # Имя переменной в шаблоне для списка объектов

class CarUpdateView(UpdateView):
    model = Car
    fields = ['brand', 'model', 'license_plate']
    template_name = 'car_form.html'
    success_url = '/cars/'  # Перенаправление после обновления

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_confirm_delete.html'  # Шаблон для подтверждения удаления
    success_url = reverse_lazy('car_list')

class CarCreateView(CreateView):
    model = Car
    template_name = 'car_create.html'  # Убедитесь, что шаблон правильный
    fields = ['brand', 'model', 'license_plate']
    success_url = '/cars/'  # Перенаправление после успешного создания


def create_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # Замените на вашу страницу после успешного создания
    else:
        form = CustomUserCreationForm()
    return render(request, 'user_form.html', {'form': form})