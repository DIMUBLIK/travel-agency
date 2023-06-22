from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home_page'),
    path('reviews/', include('reviews.urls')),
    path('contacts/', views.contacts, name='contacts'),
    path('tours/', include('applications.urls')),
]
