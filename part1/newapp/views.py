from django.shortcuts import render
from django.http import HttpResponse
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

# Create your views here.
