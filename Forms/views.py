from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {
        'form': form
        })

@login_required
def secrect_page(request):
    return render(request, 'secrect_page.html')

