from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse

# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        return HttpResponse(f'<h2>Hello, {name}!</h2>')
    else:
        userform = UserForm()
        context = {
            'form': userform
        }
        return render(request, 'form/index.html', context=context)