from django.urls import path
from . import views
urlpatterns = [
    path('',views.base,name='base'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('form/',views.form_submit,name='form_submit'),
    path('contact/',views.ContactForm,name='contact'),
    path('st_form/',views.StudentForm,name='student'),
]
