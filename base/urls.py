from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<str:pk>/', views.detail, name='detail'),
    path('create/', views.create_note, name='create'),
    path('edit/<str:pk>', views.edit_note, name='edit'),
    path('delete/<str:pk>', views.delete_note, name='delete'),
]