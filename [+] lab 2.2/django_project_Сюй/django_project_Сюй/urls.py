from django.contrib import admin
from django.urls import path, include
from project_first_app import views
from django.shortcuts import redirect

def redirect_to_admin(request):
    return redirect('/admin/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('owner/<int:owner_id>/', views.owner_detail, name='owner_detail'),
    path('', redirect_to_admin),
    path('', include('project_first_app.urls')),  # Подключение маршрутов приложения
]
