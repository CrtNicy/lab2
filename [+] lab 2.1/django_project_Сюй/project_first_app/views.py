from django.shortcuts import render, get_object_or_404
from .models import Owner

def home(request):
    return render(request, 'home.html')

def owner_detail(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    return render(request, 'owner.html', {'owner': owner})
