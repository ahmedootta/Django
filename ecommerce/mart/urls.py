from django.urls import path
from . import views

app_name = 'mart'

urlpatterns = [
    path('', views.index, name='index'),
]