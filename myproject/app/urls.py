from django.urls import path
from . import views


urlpatterns = [
    path('', views.model_list, name='model_list'),
    path('model/<str:model>/', views.model_list, name='model_list'),
    path('add_model/<str:model>/', views.add_model, name='add_model'),
]
