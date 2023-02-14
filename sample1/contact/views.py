from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Contact

def contact(request):
    contacts = Contact.objects.all()
    template = loader.get_template('contacthome.html')
    context = {
        'contacts': contacts
    }
    return HttpResponse(template.render(context,request))

def contactadd(request):
    if request.method == 'POST':
        #template = loader.get_template('contacthome.html')
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        city = request.POST['city']
        contact = Contact(name=name, mobile=mobile, email=email, city=city)
        contact.save()
        #context = {}
        #return HttpResponse(template.render(context, request))
        return redirect('contact')
    else:
        template = loader.get_template('contactadd.html')
        context = {}
        return HttpResponse(template.render(context, request))

def contactedit(request, id):
    contact = Contact.objects.get(id=id)
    if request.method == 'POST':
        #template = loader.get_template('contacthome.html')
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        city = request.POST['city']
        contact = Contact(name=name, mobile=mobile, email=email, city=city)
        contact.save()
        #context = {}
        #return HttpResponse(template.render(context, request))
        return redirect('contact')
    else:
        template = loader.get_template('contactedit.html')
        context = {
            'contact': contact
        }
        return HttpResponse(template.render(context, request))

def contactdel(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('contact')