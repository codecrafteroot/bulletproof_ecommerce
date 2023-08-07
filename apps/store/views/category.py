# builtin imports
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import Http404

# local imports
from ..models import CategoryModel
# Create your views here.

@login_required(login_url="/auth/login/")
def list(request):
    try:
        categories = CategoryModel.objects.all()
        context = {
            "title": "Categories",
            "categories": categories
        }
    except CategoryModel.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, "core/category/list.html", context)

@login_required(login_url="/auth/login/")
def category_products(request, category_id):
    try:
        category = CategoryModel.objects.get(pk=category_id)
        context = {
            "title": "Categories",
            "category": category
        }
    except CategoryModel.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, "core/category/products.html", context)