from django.shortcuts import render

from json import loads, dumps

import random

from django.http import HttpRequest
from rest_framework.decorators import api_view

from list.models import Users

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


#def index(request):
#    data = Admins.objects.all()
#    print(data)
#    return render(request, "index.html", {"data": data})

class DataView(APIView):

    def get(self, request: Request):

        inqueue = Users.objects.all().filter(queue_status='INQUEUE').order_by('queue_number')
        summoned = Users.objects.all().filter(queue_status='SUMMONED').order_by('queue_number')
        entered = Users.objects.all().filter(queue_status='ENTERED').order_by('queue_number')

        return render(request, "index.html", {"inqueue": inqueue, "summoned": summoned, "entered": entered})