import datetime,timedelta

import boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from django.http import JsonResponse, request
from django.shortcuts import render
from django.utils.crypto import get_random_string
from rest_framework import status
from rest_framework.exceptions import NotAcceptable
from django.http import JsonResponse
# Create your views here.
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Registration
from .models import Entry
from .models import Exit
from .models import History
from .models import UnregisteredVehicle

from common.apis import FullViewSet
from .serializers import EntrySerializer
from .serializers import RegiSerializer
from .serializers import ExitSerializer
from .serializers import HistroySerializer
from .serializers import HistroySerializer


class EntryViewSet(FullViewSet):
    ObjModel = Entry
    ObjSerializer = EntrySerializer

    def obj_filter(self, request):
        return Entry.objects.all()


class ExitViewSet(FullViewSet):
    ObjModel = Exit
    ObjSerializer = ExitSerializer

    def obj_filter(self, request):
        return Exit.objects.all()


class Regi(FullViewSet):
    ObjModel = Registration
    ObjSerializer = RegiSerializer

    def obj_filter(self, request):
        return Registration.objects.all()



class LogBook(APIView):

    def get(self, request, format=None):
        v_number = request.query_params.get('vehicle_number')

        if v_number is None:
            raise NotAcceptable(detail='No user id found !')

        idofregi = Registration.objects.only('id').get(vehicle_number=v_number).id
        print(idofregi)
        en = Entry.objects.filter(user_id=int(idofregi))
        ex = Exit.objects.filter(user_id=int(idofregi))

        data = {
            'Entry': EntrySerializer(en, many=True).data,
            'Exit': ExitSerializer(ex, many=True).data

        }

        return JsonResponse(data)

    def post(self, request, format=None):
        v_number = request.query_params.get('vehicle_number')
        if v_number is None:
            raise NotAcceptable(detail='No user id found !')
        try:
            obj = Registration.objects.get(vehicle_number=v_number)
            print("hello")
            en = Entry.objects.create(user_id=obj.id)

        except:
            a = UnregisteredVehicle.objects.create(urnumber=v_number)

        return JsonResponse({"vehicle_number": v_number})

class HistoryBook(APIView):
     def get(self,request, format=None):
         obj=History.objects.all()
         serializer=HistroySerializer(obj,many=True).data


         return JsonResponse(serializer,safe=False)

     def post(self, request, format=None):
         plate_number = request.query_params.get('plate_number')
         if plate_number is None:
             raise NotAcceptable(detail='No user id found !')
         try:

                 x = History.objects.filter(platenumber=plate_number).last()

                 lasttime = x.ts_created
                 timenow = datetime.datetime.now().astimezone()
                 print(lasttime)
                 print("p1")
                 print(timenow)
                 print("p2")
                 duration=timenow - lasttime
                 oneminitue =datetime.timedelta(minutes=1)
                 print(duration)
                 print("p3")
                 if(duration>oneminitue):
                     History.objects.create(platenumber=plate_number)
                     print("success")

         except:
             History.objects.create(platenumber=plate_number)



         #History.objects.create(platenumber=plate_number)
         return JsonResponse({"plate_numbe": plate_number})