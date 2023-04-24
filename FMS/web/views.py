from django.shortcuts import render
import datetime
from .models import web
from .models import login


# Create your views here.
name=''
address=''
email=''
form_no=''
current_date=''
s=''
cn1=''
cn2=''
form_no = 0
def login1(request):
    return render (request,"login.html",{'error':""})
def option(request):
    un=request.GET['un']
    pw=request.GET['pw']
    l = login.objects.get(UN=un)
    print(l.PW,"\n",l.UN)
    if(l.PW==pw and un==l.UN):
        return render(request,"option.html")
    else:
        return render(request,'login.html',{'error':"Wrong Password OR Username"})
def login2(request):
    name=request.GET['name']
    pw=request.GET['pass']
    run=request.GET['run']
    rpw=request.GET['rpw']
    print(name,"\t",pw)
    l = login.objects.get(UN=run)
    if(rpw==l.PW):
        log = login(UN=name,PW=pw)
        log.save()
        return render(request,"option.html",{'name':""})
    else:
        return render(request,"login.html",{'name':"Wrong Inputs"})

def student(request):
    data = web.objects.all()
    return render(request,"studentsearch.html",{'data': data})

def newenrollment(request):
    global form_no
    latest_record = web.objects.latest('form_no')
    formno=latest_record.form_no
    form_no=int(formno)
    form_no=form_no+1 #get from the Database
    return render(request,"newenrollment.html",{'formno':form_no})



def bookingConfirmation(request):
    global name
    global address
    global email
    global form_no
    global current_date
    global s
    global cn1
    global cn2
    global sex
    fname=request.GET['fname']
    mname=request.GET['mname']
    lname=request.GET['lname']
    name= fname+' '+mname+' '+lname
    address=request.GET['Address']    
    email=request.GET['email']
    form_no=request.GET['Formno']
    cn1= request.GET['contact1']
    cn2 = request.GET['contact2']
    sex = request.GET['Sex']
    current_date = datetime.date.today()
    cd = str(current_date)
    y=cd[0:4]
    m=cd[5:7]
    s=y+m+'00'+str(form_no)#Add two zeros before it
    return render(request,'bookingConfirmation.html', {'name':name,'address':address,'email':email,'form_no':form_no,'date':current_date,'studentid':s})

def feesrecipt(request):
    global name
    global address
    global email
    global form_no
    global current_date
    global s
    global cn1
    global cn2
    cda = str(current_date)
    y=cda[0:4]
    m=cda[5:7]
    s=y+m+'00'+str(form_no)#Add two zeros before it
    cd=request.GET['Course_Desc']
    print(cd)
    fa=request.GET['Fees']
    d = request.GET['Discount']
    afp = request.GET['AFP']
    GST = 18
    ia = request.GET['installment']
    doi=request.GET['durationofinstallment']
    fa=(int)(fa)
    d=int(d)
    gross=(fa)-((fa)*.18)
    d=fa*d/100
    gst=(fa)*.18
    t=gross+gst-d
    tfp=(int)(afp)
    rf=((int)(fa))-tfp
    ino=1
    Web = web(
                name=name, 
                address=address,
                email=email,
                form_no=form_no,
                s=s,
                course=cd,
                cdate=cda,
                cn1=cn1,
                cn2=cn2,
                sex=sex,
                fa=fa,
                ia=ia,
                d=d,
                apf=afp,
                doi=doi,
                rf=rf,
                tfp=tfp,
                ino=ino,
            )
    Web.save()
    return render(request,'feesrecipt.html',{'name':name,'course':cd,'address':address,'email':email,'form_no':form_no,'date':current_date,'studentid':s,'installment':ia,'doi':doi,'gross':gross,'d':d,'t':t,'gst':gst,'cd':cd})

def reciptform(request):
    return render(request,"reciptform.html")
def recipt(request):
    name=request.GET['name']
    mop=request.GET['yesno']
    pname=request.GET['pname']
    course=request.GET['course']
    sid=request.GET['sid']
    f=request.GET['fees']
    tid=request.GET['TID']
    current_date = datetime.date.today()
    cd = str(current_date)
    w = web.objects.get(s=sid)
    w.ino = ((int)(w.ino))+1
    w.cdate = cd
    w.tfp = ((int)(w.tfp))+int(f)
    w.rf = w.rf-int(f)
    w.save()
    return render(request,'recipt.html',{'name':name,'mop':mop,'pname':pname,'sid':sid,'course':course,'f':f,'TID':tid,'cd':cd})
def ss(request):
    sid1=request.GET['studentid']
    w = web.objects.get(s=sid1)
    return render(request,"cfp.html",{'name':w.name,'sid':w.s,'course':w.course,'f':w.fa,'tfp':w.tfp,'cdate':w.cdate,'ia':w.ia,'rf':w.rf,'ino':w.ino})
def courses(request):
    return render(request,"courses.html")