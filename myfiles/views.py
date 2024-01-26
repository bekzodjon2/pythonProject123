from django.shortcuts import render
from myfiles.models import Portfolio, Hodim, Contact


# Create your views here.

def index(malumot):
    if 'message' in malumot.POST:
        ismi = malumot.POST.get('name')
        gmail = malumot.POST.get('email')
        mavzu = malumot.POST.get('subject')
        text = malumot.POST.get('message')
        Contact(name=ismi,email=gmail,subject=mavzu,text=text).save()


    ports = Portfolio.objects.all()
    team = Hodim.objects.all()
    return render(malumot,'index.html',{"ports":ports,"team":team})
def inner_page(malumot):
    team = Hodim.objects.all()
    return render(malumot,'inner-page.html',{"team":team})

def portfolio(malumot,id):
    port = Portfolio.objects.get(id=id)
    return render(malumot,'portfolio-details.html',{"port":port})