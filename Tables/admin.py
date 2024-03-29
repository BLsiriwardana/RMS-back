from django.contrib import admin
from .models import Tables
from .models import foodcat
from .models import asignwaiters
from .models import employee
from .models import offers
from .models import fooditem

admin.site.register(Tables)
admin.site.register(foodcat)
admin.site.register(asignwaiters)
admin.site.register(employee)
admin.site.register(offers)
admin.site.register(fooditem)
# Register your models here.
