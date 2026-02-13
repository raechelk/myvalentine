from django.urls import path

from love import views

urlpatterns = [
    path('', views.home, name='home'),
]