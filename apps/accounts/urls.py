#builtin imports
from django.urls import path, include

# local imports
from .views import profile

urlpatterns = [
    path('profile', profile, name='profile'),
]