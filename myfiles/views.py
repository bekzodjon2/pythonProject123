from django.shortcuts import render
from myfiles.models import Portfolio
# Create your views here.

def index(malumot):
    ports = Portfolio.objects.all()
    return render(malumot,'index.html',{"ports":ports})
def inner_page(malumot):
    return render(malumot,'inner-page.html')
def portfolio(malumot,id):
    port = Portfolio.objects.get(id=id)
    return render(malumot,'portfolio-details.html',{"port":port})