from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewset)
router.register(r'people', views.PersonViewset)
router.register(r'addresses', views.AddressViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]