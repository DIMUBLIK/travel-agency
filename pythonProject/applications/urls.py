from django.urls import path
from . import views

urlpatterns = [
    path('', views.tours_home, name='tours_home'),
    path('application/', views.application, name='application')

]