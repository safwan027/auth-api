from django.urls import path
from . views import User1


urlpatterns = [
    path('user/',User1.as_view()),
]
