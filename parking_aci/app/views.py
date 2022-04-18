import json

import requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import Registration
from .models import Entry
from .models import Exit
from datetime import datetime
from django import forms
from .forms import UserForm
from django.contrib import messages
from .models import logbook
from .models import History

# Create your views here

def index(request):
    if request.method == 'POST':

        stuff_id = request.POST.get('stuff_id')
        full_name = request.POST.get('full_name')
        department = request.POST.get('department')
        phone_no = request.POST.get('phone_no')
        designation = request.POST.get('designation')
        vehicle_number = request.POST.get('vehicle_number')
        print(stuff_id)
        last6 = vehicle_number[-6:]
        vehicle_type = request.POST.get('vehicle')

        try:
            a = Registration.objects.create(stuff_id=stuff_id, full_name=full_name, department=department,
                                            phone_no=phone_no, designation=designation, vehicle_number=last6,
                                            vehicle_type=vehicle_type)
            a.save()
        except requests.exceptions.ConnectionError as e:
            raise Exception(e)

    return render(request, 'index.html', context=None)


def parking(request):
    if 'entry' in request.POST:
        try:
            reginumber = request.POST.get('reginumber')
            sixdigit = reginumber[-6:]
            print(reginumber)
            obj = Registration.objects.get(vehicle_number=sixdigit)
            print(obj.id)
            a = Entry.objects.create(user_id=obj.id)
            a.save()
            messages.success(request, 'Successful Entry!!')
        except Registration.DoesNotExist:
            messages.warning(request, 'User Does Not Exist')

    if 'exit' in request.POST:
        try:
            reginumber = request.POST.get('reginumber')
            sixdigit = reginumber[-6:]
            obj = Registration.objects.get(vehicle_number=sixdigit)
            print(obj.id)
            a = Exit.objects.create(user_id=obj.id)
            a.save()

            messages.success(request, 'Successful Exit!!')
            print(reginumber)
        except Registration.DoesNotExist:
            messages.warning(request, 'User Does Not Exist')

    if 'entry1' in request.POST:
        reginumber = request.POST.get('reginumber')
        obj = Registration.objects.get(vehicle_number=reginumber)
        try:
            lastobj = logbook.objects.filter(user_id=obj.id).last()
            if lastobj is None:
                a = logbook.objects.create(user_id=obj.id, status="Out")
                a.save()
            else:
                if lastobj.status == "In":
                    a = logbook.objects.create(user_id=obj.id, status="Out")
                    a.save()
                if lastobj.status == "Out":
                    a = logbook.objects.create(user_id=obj.id, status="In")
                    a.save()
        except IndexError:
            print("asds")
    return render(request, 'parking.html', context=None)


