from django.urls import path
from . import views

urlpatterns = [
    path('', views.tag_index, name='tag_index'),
]
