# builtin imports
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/auth/login/")
def index(request):
    # return HttpResponse("You're looking Great {}".format(request.user.username))
    template = loader.get_template("core/index.html")
    context = {
        "title": "Home",
    }
    return HttpResponse(template.render(context, request))