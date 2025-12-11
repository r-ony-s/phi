from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models

# Create your views here.
def mode(request):
    students=models.SampleModel.objects.all()
    print(students)
    return render(request,'new.html',{'data':students})
def delete_data(request,roll):
    std=models.SampleModel.objects.get(roll=roll).delete()
    print(std)
    return redirect('mode')
