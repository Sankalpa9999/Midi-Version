from django.urls import path
from . import views

urlpatterns = [
    path('share/', views.share_content, name='share_content'),
    path('shared/', views.view_shared_content, name='view_shared_content'),
]