from django.urls import path

from core import views
from . import views

urlpatterns = [
      path('service/', views.service, name='service' )
]