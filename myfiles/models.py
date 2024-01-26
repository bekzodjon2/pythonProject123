from django.db import models

# Create your models here.
class Title(models.Model):
    name = models.CharField(max_length=30)

class Lavozim(models.Model):
    nomi = models.CharField(max_length=30)
    def __str__(self):
        return self.nomi

class Hodim(models.Model):
    name = models.CharField(max_length=30)
    lavozim = models.ForeignKey(Lavozim,on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='media')
    tele = models.CharField(max_length=40)
    face = models.CharField(max_length=40)
    inst = models.CharField(max_length=40)
    twitter = models.CharField(max_length=40)
    data = models.DateField(auto_now=True)

class Turi(models.Model):
    turi = models.CharField(max_length=25)
    def __str__(self):
        return self.turi


class Portfolio(models.Model):
    img = models.ImageField(upload_to='media')
    Name = models.CharField(max_length=15)
    Turlari = models.ForeignKey(Turi, on_delete=models.CASCADE)
    Category = models.CharField(max_length=30)
    data = models.DateField()
    Klent = models.CharField(max_length=30)
    Link = models.CharField(max_length=30)

class Servis(models.Model):
    rasm = models.ImageField(upload_to='media')
    nomi = models.CharField(max_length=15)
    malumot = models.TextField()
    Sana = models.DateField(auto_now=True)

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateField(auto_now=True)








