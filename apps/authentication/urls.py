#builtin imports
from django.urls import path, include

# local imports
from .views import index, CompleteSignupView

urlpatterns = [
    path('', index, name='index'),
    path('auth/complete-signup/', CompleteSignupView.as_view(), name='complete_signup'),
    path('auth/', include('allauth.urls')),
]