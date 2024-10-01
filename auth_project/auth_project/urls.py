from django.urls import path
from django.contrib import admin
from . views import RegisterAPI,LoginAPI


urlpatterns = [
    path('admin/',admin.site.urls),
    path('register/',RegisterAPI.as_view()),
    path('login/',LoginAPI.as_view()), 
]

