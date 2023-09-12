from django.urls import path, include
# from .views import PersonListCreateView, PersonRetrieveUpdateDestroyView, PersonSearchByNameView
from rest_framework import routers

from . import views

# urlpatterns = [
#     path('api/', PersonListCreateView.as_view(), name='person-list-create'),
#     path('api/<int:pk>/', PersonRetrieveUpdateDestroyView.as_view(), name='person-retrieve-update-destroy'),
#     path('api/<str:name>/', PersonSearchByNameView.as_view(), name='person-search-by-name'),
# ]

app_name = 'personres'

router = routers.DefaultRouter()

router.register(r'', views.PersonViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]