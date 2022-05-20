from django.urls import path, include
from rest_framework import routers
from apis import views


router = routers.DefaultRouter()
router.register('add-data', views.AddDataViewSet, basename='adddata')
router.register('get-data', views.PopulationDataViewSet, basename='getdata')


urlpatterns = [
    path('', include(router.urls)),
]
