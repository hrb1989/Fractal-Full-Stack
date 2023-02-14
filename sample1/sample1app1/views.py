from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.template import loader
from .models import Name

def hello(request):
    names = Name.objects.all().values() #from Model
    #template = loader.get_template('hello.html')
    template = loader.get_template('names.html')
    context = {
        'names': names #to the template variable names, which is inside for loop
    }
    #return HttpResponse("Hello World!")
    #return HttpResponse(template.render())
    return HttpResponse(template.render(context, request))


def details(request, id):
    name = Name.objects.get(id=id) #from Model
    #template = loader.get_template('hello.html')
    template = loader.get_template('details.html')
    context = {
        'name': name #to the template variable names, which is inside for loop
    }
    #return HttpResponse("Hello World!")
    #return HttpResponse(template.render())
    return HttpResponse(template.render(context, request))

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def divisible(request, num1):
    template = loader.get_template('divisible.html')
    context = {
        'number': num1
    }
    return HttpResponse(template.render(context, request))

def divisible2(request, num1, num2):
    template = loader.get_template('divisible2.html')
    context = {
        'num1': num1,
        'num2': num2
    }
    return HttpResponse(template.render(context, request))