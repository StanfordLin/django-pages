from django.urls import path

from .views import HomePageView, AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),

    # Add as_view() at the end for class based views
    path('', HomePageView.as_view(), name='home'),

]
