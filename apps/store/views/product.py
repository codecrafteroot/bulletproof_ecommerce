# builtin imports
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import Http404

# local imports
from ..models import ProductModel, CategoryModel
from ..forms import ProductForm, ProductImageForm
# Create your views here.

@login_required(login_url="/auth/login/")
def list(request):
    try:
        products = ProductModel.objects.all()
        context = {
            "title": "All Products",
            "products": products
        }
    except ProductModel.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, "core/product/list.html", context)

@login_required(login_url="/auth/login/")
def listByCategory(request, category_id):
    try:
        category = CategoryModel.objects.get(pk=category_id)
        context = {
            "title": "Categories",
            "products": category.products.all()
        }
    except CategoryModel.DoesNotExist:
        raise Http404("Category does not exist")
    return render(request, "core/category/products.html", context)

@login_required(login_url="/auth/login/")
def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)  # Save the form data to the database
            item.owner = request.user
            item.save()
            return redirect('index')  # Replace 'success_url' with the URL to redirect after successful form submission.
    else:
        form = ProductForm()

    return render(request, 'core/product/create.html', {'title': 'Profile', 'form': form})

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

@login_required(login_url="/auth/login/")
def add_images(request, product_id):
    if request.method == 'POST':
        form = ProductImageForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.product = ProductModel.objects.get(pk=product_id)
            item.save()
            return redirect('product-detail', product_id=product_id)
    else:
        form = ProductImageForm()

    return render(request, 'core/product/add_images.html', {'form': form})
