from django.urls import path
from . import views
urlpatterns = [
    path('',views.mode,name='mode'),
    path('delete/<int:roll>/',views.delete_data,name='td-delete'),
]
