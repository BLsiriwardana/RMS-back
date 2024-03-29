from django.shortcuts import render
from .models import Tables
from .models import foodcat
from .models import IPaddress1
from .models import asignwaiters
from .models import employee
from .models import offers
from .models import fooditem
from .models import waitermessage
from .serializers import TableSerializer
from .serializers import IPSerializer
from .serializers import foodcatSerializer
from .serializers import asignwaitersSerializer
from .serializers import fooditemSerializer
from .serializers import employeeSerializer
from .serializers import offersSerializer
from .serializers import waitermessageSerializer
from rest_framework import viewsets
from django.http import JsonResponse
import cv2
from pyzbar.pyzbar import decode
 

class Tableview(viewsets.ModelViewSet):
    queryset = Tables.objects.all()
    serializer_class = TableSerializer


class Ipview(viewsets.ModelViewSet):
    queryset = IPaddress1.objects.all()
    serializer_class = IPSerializer 


class foodcatview(viewsets.ModelViewSet):
    queryset = foodcat.objects.all()
    serializer_class = foodcatSerializer 


class asignwaitersview(viewsets.ModelViewSet):
    queryset = asignwaiters.objects.all()
    serializer_class = asignwaitersSerializer

class employeeview(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer

class offersview(viewsets.ModelViewSet):
    queryset = offers.objects.all()
    serializer_class = offersSerializer 

class fooditemview(viewsets.ModelViewSet):
    queryset = fooditem.objects.all()
    serializer_class = fooditemSerializer

class waitermessageview(viewsets.ModelViewSet):
    queryset = waitermessage.objects.all()
    serializer_class = waitermessageSerializer

def process_frames(frame):
    decoded_objs = decode(frame)
    qr_data_list = []
    for obj in decoded_objs:
        qr_data = obj.data.decode("utf-8")
        qr_data_list.append(qr_data)
        # You can process the QR code data here
    return qr_data_list

# Define a generator function to process the video stream
def process_video_stream():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        qr_data_list = process_frames(frame)
        yield qr_data_list
    cap.release()

# Define the API view function
def qr_code_api(request):
    qr_data_list = next(process_video_stream())
    return JsonResponse({"qr_data_list": qr_data_list}) 

 