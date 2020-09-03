from django.urls import path 

from .views import HomePageViews, AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'), 
    path('', HomePageViews.as_view(), name='home'),
]

