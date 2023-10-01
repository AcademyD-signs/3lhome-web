from django.urls import path
from .views import Home, AboutUs, Gallery, ContactUs, Services
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', Home.as_view(), name='home'),    
    path('about_us', AboutUs.as_view(), name='about_us'),
    path('gallery', Gallery.as_view(), name='gallery'),
    path('contact_us', ContactUs.as_view(), name='contact_us'),
    path('services', Services.as_view(), name='services'),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)