#builtin imports
from django.urls import path, include

# local imports
from .views import index
urlpatterns = [
    path('', index, name='index'),
    path('auth/', include('allauth.urls')),
]