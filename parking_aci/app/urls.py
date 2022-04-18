
from django.urls import path, include

from rest_framework import routers
from . import apis
from common.apis import FullViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from . import views
router = routers.DefaultRouter()
router.register('entry', apis.EntryViewSet, basename='entry')
router.register('user', apis.Regi, basename='regi')
router.register('exit', apis.ExitViewSet, basename='exit')

urlpatterns = [

    path('logbook', apis.LogBook.as_view(), name="logbook"),
    path('registration', views.index, name="registration"),
    path('', views.parking, name="parking"),

    path('history',apis.HistoryBook.as_view(),name="history"),


]

urlpatterns += router.urls