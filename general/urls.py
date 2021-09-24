from django.urls.conf import include
# from .views import IndexView
from django.urls import path
from general.views import IndexView, ContactView, TermsAndConditions

app_name = 'general'

urlpatterns = [
    path('', IndexView.as_view(), name = 'home'), 
    path('contact/', ContactView.as_view(), name = 'contact'), 
    path('terms_and_conditions/', TermsAndConditions.as_view(), name = 'tandc'), 
    
]