# pages/urls.py
from django.urls import path
from .views import HomePageView, ContactPageView, AboutPageView

urlpatterns = [
        path('', HomePageView.as_view(), name='home'),
        path('about/', AboutPageView.as_view(), name='about'),
        path('contact/', ContactPageView.as_view(), name='contact'),
]
