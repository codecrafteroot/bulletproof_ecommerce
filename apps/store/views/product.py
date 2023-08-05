# builtin imports
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import Http404

# local imports
from apps.store.models import ProductModel
# Create your views here.


@login_required(login_url="/auth/login/")
def detail(request, product_id):
    try:
        product = ProductModel.objects.get(pk=product_id)
        context = {
            "title": "Product",
            "product": product
        }
    except ProductModel.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, "core/product/detail.html", context)