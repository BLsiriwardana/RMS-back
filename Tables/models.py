from django.db import models
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
import random
import numpy as np
import os
from django.db import models
from PIL import Image, ImageDraw
from multiupload.fields import MultiFileField 
from django.core.files.base import ContentFile
from django.http import JsonResponse
    
 
class Tables(models.Model):
    Code_name = models.CharField(max_length=225,primary_key=True)
    table_number =  models.CharField(max_length=225, null=True)
    max_member = models.CharField(max_length=200, null=True)
    pass_code = models.CharField(max_length=200,null=True)
    Table_catogary = models.CharField(max_length=200, null=True)
    qr_codes = models.ImageField(upload_to='qr_codes', blank=True , null=True)
    status = models.CharField(max_length=200,null=True)
    times = models.CharField(max_length=200,null=True)
    
    def save(self, *args, **kwargs):
    # Only generate QR code if qr_codes field is empty
     if not self.qr_codes:
        num = np.random.randint(1000, 10000)
        passwd = str(self.Code_name)  
        url = f"http://localhost:3000/get_table_from_app/{self.Code_name}"
        self.pass_code = passwd
    
        # Generate QR code
        QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
        QRcode.add_data(url)
        QRcode.make()
        QRcolor = 'Black'
    
        # Generate the QR code image
        QRimg = QRcode.make_image(fill_color=QRcolor, back_color="white").convert('RGB')
    
        # Save the QR code image
        buffer = BytesIO()
        QRimg.save(buffer, format='PNG')
    
        # Save the QR code image to the model field
        self.qr_codes.save(f'{passwd}.png', ContentFile(buffer.getvalue()), save=False)
    
     super().save(*args, **kwargs)

    def __str__(self) :
        return self.Code_name


#to temporary save login  records . 
class IPaddress1(models.Model):
    user_id = models.CharField(max_length=225, unique=True)
    ip_address= models.CharField(max_length=225, unique=True)
    table_id = models.CharField(max_length=225, primary_key=True)
    name = models.CharField(max_length=225, null=True)
    phone = models.CharField(max_length=225,null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    Time = models.TimeField(auto_now_add=True, null=True) 
    
     
    def __str__(self) :
        return self.ip_address    

class foodcat(models.Model):
   
    catImage = models.ImageField(upload_to='catimg',blank=False, null=True)
    cat_id = models.CharField(max_length=225, primary_key=True)
    catname= models.CharField(max_length=225)
    Description= models.CharField(max_length=225)
    time = models.TimeField(auto_now_add=True, null=True)
    add_date = models.DateField(auto_now_add=True)
    number_items = models.CharField(max_length=225, null=True) 
     
    def __str__(self) :
        return self.catname   

class asignwaiters(models.Model):
    table_id = models.CharField(max_length=225, primary_key=True)
    emp_id = models.CharField(max_length=225)
    emp_name = models.CharField(max_length=225)
    emp_status = models.CharField(max_length=225)
    temp_id = models.CharField(max_length=225)
    temp_name = models.CharField(max_length=225)
    temp_status = models.CharField(max_length=225)
    asign_date = models.DateField(auto_now_add=True)

    def __str__(self) :
        return self.emp_name
    
class waiterAssignHistory(models.Model):
    table_id = models.CharField(max_length=225)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.table_id

class employee(models.Model):
    emp_id = models.CharField(max_length=225,primary_key=True)
    catImage = models.ImageField(upload_to='employee',blank=False, null=False)
    emp_name = models.CharField(max_length=225)
    Birth = models.DateField(max_length=225)
    NIC = models.CharField(max_length=225, unique=True)
    address = models.CharField(max_length=225)
    drl = models.CharField(max_length=225,   null=True)
    phone = models.CharField(max_length=225)
    email = models.CharField(max_length=225, null=True)
    role = models.CharField(max_length=225)
    status = models.CharField(max_length=225)
    
    def __str__(self) :
        return self.emp_name

class fooditem(models.Model):
    food_id =  models.CharField(max_length=225,primary_key=True)
    foodImage = models.ImageField(upload_to='food',blank=False, null=True)
    name = models.CharField(max_length=100)
    catagory = models.CharField(max_length=225, null=True)
    description = models.TextField( )
    short_description = models.TextField(max_length=225)
    subimages = MultiFileField(max_num=3)
    price =models.CharField(max_length=100) 
    status = models.IntegerField()
    def __str__(self) :
        return self.name


class offers(models.Model):
    offer_number = models.IntegerField(primary_key=True)
    offImage = models.ImageField(upload_to='food',blank=False, null=True)
    offer_des = models.TextField()
    food_id =  models.CharField(max_length=225)
    food_name = models.CharField(max_length=225)
    started_date = models.DateField(max_length=225)
    end_date = models.DateField(max_length=225)
    status = models.IntegerField()
    def __str__(self) :
        return self.offer_number



class waitermessage(models.Model):
    emp_id = models.CharField(max_length=225)
    table_id = models.CharField(max_length=225)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    status = models.IntegerField(null=True)
    def __str__(self) :
        return self.table_id
    

class assigncat(models.Model):
    cat_id = models.CharField(max_length=225)
    food_id = models.CharField(max_length=225)
    name = models.TextField()
    price =models.CharField(max_length=100) 
    status = models.IntegerField(null=True)
    def __str__(self) :
        return self.name

class cart(models.Model):
    user_id = models.IntegerField()
    table_id = models.CharField(max_length=225)
    food_id = models.CharField(max_length=225)
    food_name = models.CharField(max_length=225)
    order_id = models.CharField(max_length=225)
    quantity = models.IntegerField()
    order_des = models.TextField(null=True)
    price = models.IntegerField()
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self) :
        return self.food_id

class order(models.Model):
    order_id = models.CharField(max_length=225)
    user_id = models.IntegerField( null=True)
    table_id = models.CharField(max_length=225, null=True)
    name = models.CharField(max_length=225, null=True)
    phone = models.CharField(max_length=225, null=True)
    waiter = models.CharField(max_length=225, null=True)
    chef = models.CharField(max_length=225, null=True)
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    payment_method = models.CharField(max_length=225, null=True)
    value = models.CharField(max_length=225, null=True)
    pay_status = models.CharField(max_length=225,null=True)
    action_status = models.CharField(max_length=225,null=True)
 
    def __str__(self) :
        return self.order_id

class Tusers(models.Model):
    user_id = models.IntegerField()
    order_id = models.CharField(max_length=225)
    Uname = models.CharField(max_length=225)
    moblie = models.CharField(max_length=225)
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    def __str__(self) :
        return self.user_id
    
 