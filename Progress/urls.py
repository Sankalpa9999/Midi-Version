from django.urls import path
from . import views

urlpatterns = [
    path('', views.progress_list, name='progress_list'),
    path('add/', views.add_progress, name='add_progress'),
    path('charts/', views.progress_charts, name='progress_charts'),
]
