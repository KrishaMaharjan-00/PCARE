from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Contact
from . models import Notification
from . models import Pressure
from win10toast import ToastNotifier
import time

# Create your views here.

def home(request):
    return render(request,'base.html')
def home2(request):
    return render(request,'pages/home.html')
def index(request):
    return render(request,'pages/about.html')
def login(request):
    return render(request,'pages/login.html')
def contact(request):
    return render(request,'pages/contact.html')
def health(request):
    return render(request,'careyourself/healthy_diet.html')
def awareness(request):
    return render(request,'careyourself/awareness.html')
def exercises(request):
    return render(request,'careyourself/exercises.html')
def pbook(request):
    return render(request,'careyourself/pbooks.html')
def vitamins(request):
    return render(request,'careyourself/vitamins.html')
def mental(request):
    return render(request,'careyourself/mental.html')
def notification(request):
    return render(request,'customers/notification.html')
def pressure(request):
    return render(request,'customers/pressure.html')
def message(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        contactInfo = Contact(name=name, email=email, message=message)
        contactInfo.save()
    return render(request,'customers/msg.html')


def message1(request): 
    if request.method == "POST":
        mname = request.POST["mname"]
        thours = request.POST["hours"]
        tminutes = request.POST["minutes"]
        tseconds = request.POST["seconds"]
        hours = int(thours)
        minutes = int(tminutes)
        seconds = int(tseconds)
        NotifyInfo = Notification(mname=mname, hours=hours, minutes=minutes, seconds=seconds)
        NotifyInfo.save()
        
    return render(request,'customers/msg1.html')


def message2(request):
    if request.method == "POST":
        name = request.POST["name"]
        tempUpperBP = request.POST["upperBP"]
        tempLowerBP = request.POST["lowerBP"]
        tempWeight = request.POST["weight"]
        upperBP = int(tempUpperBP)
        lowerBP = int(tempLowerBP)
        weight = int(tempWeight)
        NotifyInfo = Pressure(name=name, upperBP=upperBP, lowerBP=lowerBP, weight=weight)
        NotifyInfo.save()
        toaster = ToastNotifier()
        if upperBP == 120 and lowerBP == 80:
            toaster.show_toast("Your Blood Pressure Is Normal!", "Alert!", threaded=True,
                        icon_path=None, duration=3)  # 3 seconds

        
        if upperBP > 120 or lowerBP > 80:
            toaster.show_toast("Your Blood Pressure Is High!", "Alert!", threaded=True,
                        icon_path=None, duration=3)  # 3 seconds

        

        if upperBP < 120 or lowerBP < 80:
            toaster.show_toast("Your Blood Pressure Is Low!", "Alert!", threaded=True,
                        icon_path=None, duration=3)  # 3 seconds

        
    # Show notification whenever needed
    
    # To check if any notifications are active,
    # use `toaster.notification_active()`
        import time
        while toaster.notification_active():
            time.sleep(0.1)
    
    return render(request,'customers/msg2.html')

    
        
        