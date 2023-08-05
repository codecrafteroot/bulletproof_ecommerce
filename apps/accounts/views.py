# builtin imports
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/auth/login/")
def profile(request):
    template = loader.get_template("core/user/profile.html")
    context = {
        "title": "Profile",
    }
    return HttpResponse(template.render(context, request))