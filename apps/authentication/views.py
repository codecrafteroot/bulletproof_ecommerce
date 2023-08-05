# builtin imports
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/auth/login/")
def index(request):
    return HttpResponse("You're looking Great {}".format(request.user.username))