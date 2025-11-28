from django.shortcuts import render
from django.http import HttpResponse
from .forms import SampleForm, StudentData
def base(request):
    return render(request, 'base.html')
def home(request):
    return render(request, 'home.html')

def about(request):
     if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('username')
        email = request.POST.get('email')
        selected_option = request.POST.get('select')
        return render(request, 'about.html', {'name': name, 'email': email, 'selected_option': selected_option})
     else:
        return render(request, 'about.html', {'name': name, 'email': email})
def form_submit(request):
        return render(request, 'form.html')
def ContactForm(request):
    if request.method == 'POST':
        form=SampleForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            
    else:
        form=SampleForm()
    return render(request, 'contact.html', {'form': form})
# Create your views here.

def StudentForm(request):
    if request.method == 'POST':
        form=StudentData(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            
    else:
        form=StudentData()
    return render(request, 'contact.html', {'form': form})
