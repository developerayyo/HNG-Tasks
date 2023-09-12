from django.urls import path
from . import views

app_name = 'endpointapp'

urlpatterns = [
    path('stage1/', views.get_info, name='get_info'),
]