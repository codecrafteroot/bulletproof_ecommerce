# builtin imports
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import Http404

# local imports
from ..models import StoreModel
from ..forms import StoreForm

# Create your views here.

@login_required(login_url="/auth/login/")
def create(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)  # Save the form data to the database
            item.owner = request.user
            item.save()
            return redirect('index')  # Replace 'success_url' with the URL to redirect after successful form submission.
    else:
        form = StoreForm()

    return render(request, 'core/store/create.html', {'title': 'Create Store', 'form': form})

@login_required(login_url="/auth/login/")
def myStore(request):
    try:
        mystore = StoreModel.objects.get(owner=request.user)
        context = {
            "title": "My Store",
            "mystore": mystore
        }
    except StoreModel.DoesNotExist:
        raise Http404("Store does not exist")
    return render(request, "core/store/mystore.html", context)