from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 

from django.views.generic import TemplateView
from django.views import generic

from hitcount.views import HitCountDetailView

from .models import Phone

class HomePageView(TemplateView):
    template_name = 'portal/home.html'

class AboutPageView(TemplateView):
    template_name = 'portal/about.html'

class PhoneDetailView(generic.DetailView):
    slug_field = 'phonenum'
    slug_url_kwarg = 'phonenum'
    model = Phone
    count_hit = True
    template_name = 'portal/detail.html'

# class PhoneSearchView(generic.ListView):
    
#     def get_queryset(self):
#         return Phone.objects.filter(phonenum__startswith=request)