# builtin imports
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

#local imports
from .models import UserModel
from .forms import UserChangeForm

# Create your views here.

@login_required(login_url="/auth/login/")
def profile(request):
    template = loader.get_template("core/user/profile.html")
    context = {
        "title": "Profile",
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="/auth/login/")
def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('profile')  # Replace 'success_url' with the URL to redirect after successful form submission.
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, 'core/user/edit_profile.html', {'title': 'Profile', 'form': form})