from django.shortcuts import render,redirect
from  trial1.models  import Contact
# from .forms import ContactForm

def contact_mysite(request):
     obj = Contact()
     obj.name = 'AYSHA'
     obj.email = 'ayshaasif14@gmail.com'
     obj.save()

     context = { 'form' : obj}
     return render(request,'display.html',context)