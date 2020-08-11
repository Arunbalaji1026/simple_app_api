from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .forms import SimpleForm
from django.contrib import messages

# Create your views here.

def customform(request):
    form = SimpleForm()
    if request.method == 'POST':
        form = SimpleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form sucessfully submitted')
        else:
            form =SimpleForm()

    form = SimpleForm
    context = {'form':form}
    return render(request,'index.html', context)
