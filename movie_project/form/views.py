from django.shortcuts import render
from .forms import UserForm
from .models import User
from django.http import HttpResponse

# Create your views here.

def index(request):
    userform = UserForm()
    context = {
        'form': userform
    }
    if request.method == 'POST':
        user = User()
        user.name = request.POST.get('name')
        user.age = request.POST.get('age')
        user.save()
        return render(request, 'form/index.html', context=context)
    else:
        return render(request, 'form/index.html', context=context)

def form_output(request):
    form_output = User.objects.all()
    context = {
        'form_output': form_output
    }
    return render(request, 'form/form_output.html', context=context)