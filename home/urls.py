from django.urls import path
from . import views


urlpatterns = [
    path('buttons/', views.buttons, name='buttons-form'),
    path('delete/', views.delete_button, name='delete-button'),
    path('', views.home, name='home'),
]
