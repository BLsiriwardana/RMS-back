from django.shortcuts import render,redirect
from .models import Tables
from .models import foodcat
from .models import IPaddress1
from .models import asignwaiters
from .models import employee
from .models import offers
from .models import fooditem
from .models import waitermessage
from .models import cart
from .models import order
from .models import topfooditem
from .serializers import TableSerializer
from .serializers import IPSerializer
from .serializers import foodcatSerializer
from .serializers import asignwaitersSerializer
from .serializers import fooditemSerializer
from .serializers import employeeSerializer
from .serializers import offersSerializer
from .serializers import waitermessageSerializer
from .serializers import orderSerializer
from .serializers import cartSerializer
from .serializers import *
from .models import *
from rest_framework import viewsets
from django.http import JsonResponse
import cv2
from pyzbar.pyzbar import decode
from .serializers import TusersSerializer
from .models import Tusers
from rest_framework.response import Response
from django.http import JsonResponse

from rest_framework.decorators import api_view
import datetime
from datetime import date
from .forms import FoodCatForm
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


class orderview(viewsets.ModelViewSet):
    queryset = order.objects.all()
    serializer_class = orderSerializer


class cartview(viewsets.ModelViewSet):
    queryset = cart.objects.all()
    serializer_class = cartSerializer

class topfooditemview(viewsets.ModelViewSet):
    queryset = topfooditem.objects.all()
    serializer_class = topfooditemSerializer


class Tusersview(viewsets.ModelViewSet):
    queryset = Tusers.objects.all()
    serializer_class = TusersSerializer

class POSorderview(viewsets.ModelViewSet):
    queryset = POSorder.objects.all()
    serializer_class = POSorderSerializer

class POScartview(viewsets.ModelViewSet):
    queryset = POScart.objects.all()
    serializer_class = POScartSerializer

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


@api_view(['GET'])
# Define the API view function
def qr_code_api(request):
    qr_data_list = next(process_video_stream())
    return JsonResponse({"qr_data_list": qr_data_list}) 



def get_records_by_user_id(request):
    user_id = request.GET.get('user_id')
    records = IPaddress1.objects.filter(user_id=user_id).values()
    return JsonResponse(list(records), safe=False)
 
def get_records_by_food_id(request):
    food_id = request.GET.get('food_id')
    records = cart.objects.filter(food_id=food_id).values()
    return JsonResponse(list(records), safe=False)

def get_order_count(request):
    # Retrieve table_id from request parameters
    table_id = request.GET.get('table_id', None)

    if table_id is not None:
        # Filter orders by current date and the provided table_id, and count the number of records
        order_count = order.objects.filter(table_id=table_id).count()
        return JsonResponse({'order_count': order_count})
    else:
        # If table_id is not provided, return an error response
        return JsonResponse({'error': 'table_id is required'}, status=400)

def get_pos_order_count(request):
    order_count = POSorder.objects.all().count()
    return JsonResponse({'POS_order_count': order_count})

def get_order_by_id(request, order_id):
    try:
        # Retrieve order based on the provided order_id
        order = order.objects.get(order_id=order_id)
        order_data = {
            'id': order.id,
            'order_id': order.order_id,
            'user_id': order.user_id,
            'table_id': order.table_id,
            'name': order.name,
            'phone': order.phone,
            'time': order.time.strftime('%H:%M:%S'),
            'date': order.date.strftime('%Y-%m-%d'),
            'payment_method': order.payment_method,
            'value': order.value,
            'pay_status': order.pay_status
        }
        return JsonResponse(order_data)
    except order.DoesNotExist:
        return JsonResponse({'error': 'Order not found'}, status=404)

def get_cart_items(request):
        order_id = request.GET.get('order_id', None)
        records = cart.objects.filter(order_id= order_id).values()
        return JsonResponse(list(records), safe=False)
    
def get_data(request):
    # Retrieve session information
    session_phone = request.session.get('phoneNumber')
    session_name = request.session.get('name')
    session_user_id = request.session.get('ipid')
    dd='23'
    # Query data based on session information
    queryset = order.objects.filter(user_id=session_user_id)

    # Serialize queryset
    data = [{'order_id': obj.order_id, 'table_id': obj.table_id} for obj in queryset]

    return JsonResponse(data, safe=False)

 
 

def get_chef_employees(request):
    chef_employees = employee.objects.filter(role__iexact="chef").values()
    return JsonResponse(list(chef_employees), safe=False)

def get_waiter_employees(request):
    waiter_employees = employee.objects.filter(role__iexact="waiter").values()
    return JsonResponse(list(waiter_employees), safe=False)

def add_food_category(request):
    if request.method == 'POST':
        form = FoodCatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to success page after successful form submission
    else:
        form = FoodCatForm()
    return render(request, 'add_food_category.html', {'form': form})


def get_count(request):
    # Retrieve table_id from request parameters
  #  POSorder_id = request.GET.get('order_id', None)
    POSorder_id = 'POS002'
    if POSorder_id is not None:
        # Filter orders by current date and the provided table_id, and count the number of records
        order_count = POScart.objects.filter(order_id=POSorder_id ).count()
        if order_count == 0 :
           return JsonResponse({'empty_order_count': order_count})
        else:
           return JsonResponse({'order_count': order_count})
    else:
        # If table_id is not provided, return an error response
        return JsonResponse({'error': 'table_id is required'}, status=400)
    

def get_records_pos_id(request):
    value = request.GET.get('value')
    num1_str, num2_str = value.split('_')
    records = POScart.objects.filter(order_id=num1_str, food_id=num2_str ).values()
    return JsonResponse(list(records), safe=False)


def get_records_pos_order(request):
    value = request.GET.get('value')
    records = POScart.objects.filter(order_id=value).values()
    return JsonResponse(list(records), safe=False)

def delete(request):
    quary = cart.objects.all()
    quary.delete()
    records = cart.objects.all()
    return JsonResponse(list(records), safe=False)



from django.http import JsonResponse
from .models import POScart

import datetime

 
def get_records_pos_order_daily(request):
    x = datetime.datetime.now()
    date = x.date()

# Get the first day of the current month
    first_day_of_month = date.replace(day=1)

# Get the last day of the current month
    last_day_of_month = first_day_of_month.replace(
    month=first_day_of_month.month % 12 + 1,
    day=1
) - datetime.timedelta(days=1)

# Delete existing records in topfooditem
    topfooditem.objects.all().delete()

# Retrieve records from the POScart model for the current month
    records = POScart.objects.filter(date__range=[first_day_of_month, last_day_of_month]).values_list('food_id', flat=True)
    recordssecond = cart.objects.filter(date__range=[first_day_of_month, last_day_of_month]).values_list('food_id', flat=True)
    # Count occurrences of each food ID
    array_1 = []
    for x in records:
          array_1.append(x)
    
    array_2 = []
    for y in recordssecond:
          array_2.append(y)

    combined = array_2 + array_1
   
    count_dict = {}
    for food_id in combined:
        count_dict[food_id] = count_dict.get(food_id, 0) + 1

    
    # Sort the dictionary based on the counts in descending order
    sorted_dict = dict(sorted(count_dict.items(), key=lambda item: item[1], reverse=True))
     
    
    response_data = []
    for food_id, quantity in sorted_dict.items():
        response_data.append({"foodid": food_id, "quantity": quantity})



    final = []
    x = 0
    length = len(response_data)
    while True:
        if(x == length):
            break
        else:
            data = response_data[x]
            fdata = data['foodid']
            final.append(fdata)
            x += 1
    
    y = 0
    last = []
    range = final[0:5]
    length_final = len(range)
    while True:
        if( y==length_final ):
            break
        else:
            records = fooditem.objects.get(food_id=range[y])
            response = {
                "food_id":records.food_id,
                "name":records.name
            }
            topfooditem.objects.create(
                food_id=records.food_id,
                foodImage=records.foodImage,
                name=records.name,
                catagory=records.catagory,
                description=records.description,
                short_description = records.short_description,
                price = records.price,
                status = records.status
                
                # Add more fields as needed
            )
            
            last.append(response)
            y += 1
    
    
    # Return the JsonResponse with the formatted data
    return JsonResponse(sorted_dict, status=200, safe=False)
