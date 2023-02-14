from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('hello/details/<int:id>', views.details, name='details'),
    #path('', views.home, name='home'),
    path('divisible/<int:num1>', views.divisible, name="divisible"),
    path('divisible2/<int:num1>/<int:num2>', views.divisible2, name="divisible2")
]