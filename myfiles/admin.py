from django.contrib import admin

# Register your models here.
from myfiles.models import *


class AdminHodim(admin.ModelAdmin):
    list_display = ['name', 'lavozim', 'text', 'image', 'tele', 'face', 'inst', 'twitter', 'data']


admin.site.register(Hodim, AdminHodim)


class AdminLavozim(admin.ModelAdmin):
    list_display = ['nomi']


admin.site.register(Lavozim, AdminLavozim)


class AdminPortfolio(admin.ModelAdmin):
    list_display = ['img', 'Name', 'Turlari', 'Category', 'data', 'Klent', 'Link']


admin.site.register(Portfolio, AdminPortfolio)


class AdminServis(admin.ModelAdmin):
    list_display = ['rasm', 'nomi', 'malumot', 'Sana']


admin.site.register(Servis, AdminServis)


class AdminTur(admin.ModelAdmin):
    list_display = ['turi']


admin.site.register(Turi, AdminTur)

class AdminContact(admin.ModelAdmin):
    list_display = ['name','email','subject','text','date']
admin.site.register(Contact,AdminContact)