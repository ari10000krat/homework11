from django.urls import path

from . import views

urlpatterns = [
    path('', views.editor_index, name='editor_index'),
]
