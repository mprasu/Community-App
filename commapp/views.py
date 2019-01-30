from django.shortcuts import render
from .models import Details,Events
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail

def index(request):
    return render(request,'home.html')


def insert(request):
    # query1 = request.GET['query']
    # myprofile1 = Details.objects.all()
    if request.method=="POST":
        firstname1=request.POST['t1']
        lastname1 = request.POST['t2']
        usertname1 = request.POST['t3']
        phonenumber1 =int(request.POST['t4'])
        email1=request.POST['t5']
        password1=request.POST['t6']
        gender1=request.POST['t7']
        caste1=request.POST['t8']
        address1=request.POST['t9']
        district1=request.POST['t10']
        state1=request.POST['t11']
        f=Details(Firstname=firstname1,Lastname=lastname1,Username=usertname1,Phonenumber=phonenumber1,Email=email1,Gender=gender1,Password=password1,
                  Caste=caste1,Address=address1,District=district1,State=state1)
        f.save()
        m = request.POST['t5']
        subject = "Registration conformation for CApp"
        contact_message = "Thank you for using our services"
        From_email = settings.EMAIL_HOST_USER
        To_email = [m]
        send_mail(subject, contact_message, From_email, To_email, fail_silently=False)
        return render(request,'login.html')

        # def mail(request):
        #     if request.method == "POST":
        #         m = request.POST.get('t5')
        #         d1 = Details.objects.get(Email__iexact=m)
        #         if d1:
        #             if d1.Email==m:
        #                 return render(request, 'afterlogin.html')
        #             else:
        #                 return render(request,'invalid Mailid')

        # return render(request, 'login.html')
    return render(request,'sign.html')

def login(request):
    if request.method == "POST":
        un = request.POST.get('t21')
        pwd = request.POST.get('t22')
        d=Details.objects.get(Username__iexact=un)
        msg = "INVALID DETAILS"
        if d:
            if d.Username == un and d.Password == pwd:
                return render(request, 'afterlogin.html')
            else:
                return render(request,'login.html',{'msg1':msg})
    return render(request, 'login.html')

def search(request):
    if request.method == "POST":
        a1 = request.POST.get('uname')
        print("obj",a1)
        a2 = request.POST.get('location')
        match=Details.objects.filter(Address__contains=a2,Firstname__contains=a1)
        msg="No result found..."
        if match:
            return render(request, "afterlogin.html",{'newmatch':match})
        else:
            return render(request, "afterlogin.html",{'msg1':msg})

    return render(request, "search.html")

def alphabet(request):
    l=[]
    for ascii in range(65,91):
        l.append(chr(ascii))
    return render(request,'alphabetical.html',{'letters':l})

def filter_data(request):
    query1=request.GET['query']
    f=Details.objects.filter(Username__startswith=query1)
    return render(request,'filter.html',{'f1':f})


def cpassword(request):
    if request.method == 'POST':
        email = request.POST.get('a1')
        oldPassword = request.POST.get('a2')
        password = request.POST.get('a3')
        confirmPassword = request.POST.get('a4')
        mydata = Details.objects.all()
        x = 0
        for i in mydata:
            if i.Email == email:
                x = x + 1
                if i.Password == oldPassword:
                    x = x + 1
        if x == 0:
            return render(request, "changepassword.html", {'mailDoesnotExist': "mailDoesnotExist"})
        if x == 1:
            return render(request, "changepassword.html", {'wrongPassword': "Enter valid password"})
        else:
            i.Password = password
            i.ConfirmPassword = confirmPassword
            i.save()
            return render(request, "changepassword.html", {'success': "Successfully your password is changed"})
    return render(request,'changepassword.html')


def editprofile(request):
     e1 = request.POST.get('uname')
     fltr = Details.objects.filter(Username__exact=e1)

     if request.method == 'POST':
         phonenumber1 = request.POST['t4']
         email1 = request.POST['t5']
         address1 = request.POST['t9']
         district1 = request.POST['t10']
         state1 = request.POST['t11']
         mydb = Details.objects.all()
         z = 0
         for j in mydb:
            if j.Email == email1:
                 z = z + 1
            if z == 1:
                j.Phonenumber = phonenumber1
                j.Email = email1
                j.Address = address1
                j.District = district1
                j.State = state1
                j.save()
                return render(request, 'afterlogin.html', {'success': "success"})
     return render(request, 'editprofile.html', )
def events(request):
    if request.method=="POST":
        bname=request.POST.get('a1')
        beventname = request.POST.get('a2')
        bdate = request.POST.get('a3')
        btime = request.POST.get('a4')
        bdesc=request.POST.get('a5')
        mydb = Events.objects.all()
        print(bdate)
        print(btime)
        x = 0
        for i in mydb:
            j = str(i.Date)
            f = j.split('-')  # -->spliting model date
            ij = str(bdate)
            ik = ij.split('-')  # -->spliting html date
            m = str(i.Time)
            mm = m.split(':')
            n = str(btime)
            nn = n.split(':')

            if f[0] == ik[0] and f[1] == ik[1] and f[2] == ik[2]:
                if mm[0] == nn[0]:
                    print(f[0], ik[0])
                    x = x + 1
        if x == 1:
            msg = "This shift is alredy booked please choose another shift"
            return render(request, 'bookings.html', {'msg': msg})
        else:
            b=Events(Name=bname,Eventname=beventname,Date=bdate,Time=btime,Description=bdesc)
            b.save()
        return render(request,'afterlogin.html')
    return render(request,'bookings.html')

def myprofile(request,id):
    members = Details.objects.get(id=id)
    return render(request,'myprofile.html',{'members': members})



def logout(request):
    return render(request,'login.html')




