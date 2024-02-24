from django.urls import path
from .views import homepage,process_csv

urlpatterns = [
    path('', homepage, name='homepage'),
    path('upload/', process_csv, name='process_csv'),
]
