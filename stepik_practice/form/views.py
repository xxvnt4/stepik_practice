from django.shortcuts import render, reverse, redirect
from .forms import UserForm
from .models import User

# Create your views here.

def index(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = User(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age']
            )
            user.save()
            return redirect('form_output')
    else:
        form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'form/index.html', context)

def form_output(request):
    form_output = User.objects.all()
    context = {
        'form_output': form_output
    }
    return render(request, 'form/form_output.html', context=context)