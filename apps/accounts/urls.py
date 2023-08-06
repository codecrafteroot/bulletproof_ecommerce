#builtin imports
from django.urls import path, include

# local imports
from .views import profile, edit_profile

urlpatterns = [
    path('profile', profile, name='profile'),
    path('edit_profile', edit_profile, name='edit-profile'),
]