from rest_framework import serializers
from .models import Tables
from .models import foodcat
from .models import asignwaiters
from .models import IPaddress1
from .models import employee
from .models import offers
from .models import fooditem
from .models import waitermessage
from .models import cart
from .models import order
from .models import Tusers
from .models import *


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tables
        fields = '__all__'
        
class IPSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPaddress1
        fields = '__all__'

class foodcatSerializer(serializers.ModelSerializer):
    class Meta:
        model = foodcat
        fields = '__all__'


class asignwaitersSerializer(serializers.ModelSerializer):
    class Meta:
        model = asignwaiters
        fields = '__all__'
 

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = '__all__'


class offersSerializer(serializers.ModelSerializer):
    class Meta:
        model = offers
        fields = '__all__'
 
 
class fooditemSerializer(serializers.ModelSerializer):
    class Meta:
        model = fooditem
        fields = '__all__'

 
class waitermessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = waitermessage
        fields = '__all__'
class cartSerializer(serializers.ModelSerializer):
    class Meta:
        model = cart
        fields = '__all__'
class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = '__all__'
class TusersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tusers
        fields = '__all__'

class waiterAssignHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = waiterAssignHistory
        fields = '__all__'
  