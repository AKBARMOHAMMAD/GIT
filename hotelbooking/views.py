from django.shortcuts import render
from .models import Room
from .models import Check_Availability
from .models import UserRegister
from .models import Contact
from .models import Display
#from .models import Cancel


# Create your views here.
def openHomePage(request):
    type="home"
    qs = Room.objects.all()
    return render(request,"index.html",{"type":type,"qs":qs})
def openUserLogin(request):
    type=request.GET.get("type")
    return render(request,"index.html",{"type":type})
def openUserRegister(request):
    type=request.GET.get("type")
    return render(request,"index.html",{"type":type})
def openServicesPage(request):
    type=request.GET.get("type")
    return render(request,"index.html",{"type":type})
def openContactPage(request):
    type=request.GET.get("type")
    return render(request,"index.html",{"type":type})
def openCancelPage(request):
    type=request.GET.get("type")
    return render(request,"index.html",{"type":type})
def openCheck_Availability(request):
    type=request.GET.get("type")
    return render(request,"index.html",{"type":type})
#==================================================================================
def registerUser(request):
    u_fname=request.POST.get('u_fname')
    u_lname=request.POST.get('u_lname')
    u_email=request.POST.get('u_email')
    u_pass=request.POST.get('u_pass')
    u_rpass=request.POST.get('u_rpass')
    u_cno=request.POST.get('u_cno')
    u_add=request.POST.get('u_add')
    #print(u_fname,u_lname,u_email,u_pass,u_pass,u_rpass,u_cno,u_add)
    ur=UserRegister(fname=u_fname,lname=u_lname,email_id=u_email,password=u_pass,rpassword=u_rpass,contact_no=u_cno,address=u_add)
    ur.save()
    return render(request,"index.html",{"type":'h_user',"message":'User Register Successfully'})
#============================================================================================
def loginUser(request):
    username=request.POST.get('email')
    password=request.POST.get('pass')
    res=UserRegister.objects.filter(email_id=username,password=password)
    #print(res)
    if not res:
        return render(request,'index.html',{"type":'h_user',"message":'Invalid'})
    else:
        for x in res:
            print(x)

        return render(request,'index2.html',{"type":'type',"name":x})

#======================================================================================================
def ContactPage(request):
    u_name=request.POST.get('u_name')
    u_email=request.POST.get('u_email')
    u_phone=request.POST.get('u_phone')
    u_mess=request.POST.get('u_mess')
    #print(u_name,u_email,u_phone,u_phone,u_mess)
    uc=Contact(name=u_name,Email_id=u_email,phone_no=u_phone,message=u_mess)
    uc.save()
    print(uc)
    return render(request,'index.html',{"type":'h_contact',"message":'Successfully message sent'})
#=============================================================================
def openUserHomePage(request):
    type="home"
    res = UserRegister.objects.filter()
    for x in res:
        print(x)
    return render(request,"index2.html",{"type":type,"name":x})

def openBookingPage(request):
    type = request.GET.get("type")
    qs=Room.objects.all()
    res = UserRegister.objects.filter()
    for x in res:
        print(x)
    return render(request, "index2.html", {"type": type,"qs":qs,"name":x})

def openPaymentPage(request):
    type=request.GET.get("type")
    res=UserRegister.objects.filter()
    qs = Room.objects.all()
    for x in res:
        print(x)
    return render(request,"index2.html",{"type":type,"name":x,"qs":qs})
def displayPage(request):
    userName=request.GET.get("user_name")
    roomname=request.GET.get("room_type")
    checkIn=request.GET.get("check_In")
    checkOut=request.GET.get("check_Out")
    totalCost=request.GET.get("total_cost")
    custId=request.GET.get("cust_id")
    ak=Display(user_name=userName,room_type=roomname,check_In=checkIn,check_Out=checkOut,total_cost=totalCost,cust_id=custId)
    ak.save()
    return render(request,"index2.html",{"type":"display"})







def openCancelPage(request):
    u_uname=request.POST.get('user_name')
    u_roomno=request.POST.get('room_no')
    u_cust=request.POST.get('cust_id')
    print(u_uname,u_roomno,u_cust)
    bc=Cancel(user_name=u_uname,room_no=u_roomno,cust_id=u_cust)
    bc.save()
    print(bc)
   # type=request.GET.get("type")
    return render(request,"index2.html",{"type":'u_cancel',"message":'Successfully Canceled Room'})
#================================================================================