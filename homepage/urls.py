from django.urls import path
from .views import homepage,process_csv,fun_0001,fun_0002,fun_0003,fun_0004

urlpatterns = [
    path('', homepage, name='homepage'),
    path('upload/', process_csv, name='process_csv'),
    path('submit_function_0001', fun_0001, name='fun_0001'),
    path('submit_function_0002', fun_0002, name='fun_0002'),
    path('submit_function_0003', fun_0003, name='fun_0003'),
    path('submit_function_0004', fun_0004, name='fun_0004'),

]
