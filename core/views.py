from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class Home(TemplateView):
    template_name = 'index.html'

class AboutUs(TemplateView):
    template_name = 'about_us.html'

class Services(TemplateView):
    template_name = 'services.html'

class Gallery(TemplateView):
    template_name = 'gallery.html'

class ContactUs(TemplateView):
    template_name = 'contact.html'


