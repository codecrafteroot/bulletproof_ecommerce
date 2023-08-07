# builtin imports
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# local imports
from apps.store.models import ProductModel, CategoryModel
# Create your views here.


@login_required(login_url="/auth/login/")
def index(request):
    # return HttpResponse("You're looking Great {}".format(request.user.username))
    products = ProductModel.objects.all()
    categories = CategoryModel.objects.all()
    template = loader.get_template("core/index.html")
    context = {
        "title": "Home",
        "products": products,
        "categories": categories,
    }
    return HttpResponse(template.render(context, request))