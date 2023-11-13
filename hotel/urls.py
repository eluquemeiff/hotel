from django.urls import path
from . import views

urlpatterns = [
    path('', views.vue_hotel, name='vue_hotel'),
    path('client/<int:id>/', views.client_detail, name='client_detail'),
]