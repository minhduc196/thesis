from django.contrib import admin
from .models import Phone, Report, Category

# Register your models here.

admin.site.register(Phone)
admin.site.register(Report)
admin.site.register(Category)