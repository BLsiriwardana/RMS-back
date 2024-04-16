"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Tables.views import Tableview
from Tables.views import Ipview 
from Tables.views import foodcatview
from Tables.views import asignwaitersview
from Tables.views import employeeview
from Tables.views import fooditemview
from Tables.views import offersview
from Tables.views import waitermessageview
from Tables.views import cartview
from Tables.views import orderview 
from rest_framework import routers
from Tables.views import get_records_by_user_id
from Tables.views import get_records_by_food_id
from Tables.views import Tusersview
from Tables.views import get_order_count
from Tables.views import get_order_by_id
from Tables.views import get_cart_items
from Tables.views import get_data
from Tables.views import get_chef_employees
from Tables.views import add_food_category
from Tables.views import POSorderview
from Tables.views import POScartview
from Tables.views import get_pos_order_count
from Tables.views import get_count
from Tables.views import get_records_pos_id
from Tables.views import get_records_pos_order
from Tables.views import get_waiter_employees
route = routers.DefaultRouter()
route.register("",Tableview, basename="Table View")

Iproute = routers.DefaultRouter()
Iproute.register("",Ipview, basename="ip View")


foodcatroute = routers.DefaultRouter()
foodcatroute.register("",foodcatview, basename="food catagory View")


asignwaitersviewroute = routers.DefaultRouter()
asignwaitersviewroute.register("",asignwaitersview, basename="waiters asign View")


employeeroute = routers.DefaultRouter()
employeeroute.register("",employeeview, basename="employee View")

offersroute = routers.DefaultRouter()
offersroute.register("",offersview, basename="offers View")

fooditemroute = routers.DefaultRouter()
fooditemroute.register("",fooditemview, basename="fooditem View")

waitermessageroute = routers.DefaultRouter()
waitermessageroute.register("",waitermessageview, basename="offers View")

cartroute = routers.DefaultRouter()
cartroute.register("",cartview, basename="offers View")

orderroute = routers.DefaultRouter()
orderroute.register("",orderview, basename="offers View")

Tusersroute = routers.DefaultRouter()
Tusersroute.register("",Tusersview, basename="user View")

POSordeRroute = routers.DefaultRouter()
POSordeRroute.register("",POSorderview, basename="POS View")

POScartRroute = routers.DefaultRouter()
POScartRroute.register("",POScartview, basename="POS cart View")

urlpatterns = [
    path('', include('Tables.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
    path('ip/records/', get_records_by_user_id, name='get_records_by_user_id'),
    path('ip/', include(Iproute.urls)),
    path('cat/', include(foodcatroute.urls)),
    path('await/', include(asignwaitersviewroute.urls)),
    path('empl/', include(employeeroute.urls)),
    path('off/', include(offersroute.urls)),
    path('food/', include(fooditemroute.urls)),
    path('wm/', include(waitermessageroute.urls)),
    path('message/', include(waitermessageroute.urls)),
    path('carts/', include(cartroute.urls)),    
    path('records/', get_records_by_food_id, name=' get_records_by_food_id'),
    path('order/', include(orderroute.urls)),    
    path('tusers/', include(Tusersroute.urls)), 
    path('get_order_count/', get_order_count, name='get_order_count'),
    path('get_order_by_id/<str:order_id>/', get_order_by_id, name='get_order_by_id'),
    path('getcart/', get_cart_items, name='get_cart_items'),
    path('get_data/', get_data, name='get_data'),
    path('chef_employees/', get_chef_employees, name='chef-employees'),
     path('waiter_employees/', get_waiter_employees, name='waiter-employees'),
    path('add-food-category/', add_food_category, name='food category'),
    path('get_pos_count/', get_pos_order_count, name='POS count'),
    path('pos_order/', include(POSordeRroute.urls)),
    path('pos_cart/', include(POScartRroute.urls)),
    path('more_count/', get_count, name='counts'),
    path('pos_records/', get_records_pos_id, name='cart filter'),
    path('pos_orders_time/', get_records_pos_order, name='cart filter'),
]+static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)

