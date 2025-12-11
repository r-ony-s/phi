from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def mode(request):
    students=models.SampleModel.objects.all()
    print(students)
    return render(request,'new.html',{'data':students})
