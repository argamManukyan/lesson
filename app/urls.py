from django.urls import path
from .views import *


urlpatterns = [
    path('', lessons, name='homepage'),
    path('contactus/', contact_us, name='contact_us'),
    # path('gallery/', gallery, name='gallery'),
    path('test/', test, name='test'),
    path('class/<id>/', class_details, name='class_details')
]