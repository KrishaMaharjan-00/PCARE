from django.contrib import admin
from . models import Contact
from . models import Notification
from . models import Pressure
# Register your models here.
admin.site.register(Contact)
admin.site.register(Notification)
admin.site.register(Pressure)