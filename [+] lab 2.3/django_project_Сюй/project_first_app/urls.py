from django.urls import path
from . import views
from .views import owner_list, owner_create, owner_update, owner_delete, CarListView, CarUpdateView, CarDeleteView, CarCreateView, create_user

urlpatterns = [
    path('owner/<int:owner_id>/', views.owner_detail, name='owner_detail'),
    path('owners/', views.owner_list, name='owner_list'),
    path('owners/create/', owner_create, name='owner_create'),
    path('owners/<int:pk>/update/', owner_update, name='owner_update'),
    path('owners/<int:pk>/delete/', owner_delete, name='owner_delete'),
    path('cars/', CarListView.as_view(), name='car_list'),

    # Маршрут для обновления автомобиля
    path('cars/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),

    path('cars/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),

    path('cars/create/', CarCreateView.as_view(), name='car_create'),

    path('users/create/', create_user, name='user_create'),
]
