import pyrebase
from django.shortcuts import render,redirect

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
#from .models import Signin

#from .forms import SigninForm
from django.contrib import auth
config = {
    'apiKey': "AIzaSyCf6-bwCFhwlEIUnB9iknsXp5TtvN5AvRU",
    'authDomain': "test3-44aae.firebaseapp.com",
    'databaseURL': "https://test3-44aae.firebaseio.com",
    'projectId': "test3-44aae",
    'storageBucket': "test3-44aae.appspot.com",
    'messagingSenderId': "762001228928",
    'appId': "1:762001228928:web:57fb68b28ca2099a035265",
    'measurementId': "G-LD795LELXW"
}
firebase = pyrebase.initialize_app(config)
authe= firebase.auth()

db=firebase.database()


def home(request):
    return render(request, 'welcome.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def check(request):
    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    timestamps=db.child('users').child(a).child('reports').shallow().get(idtoken).val()
    print(timestamps)
    return render(request,'home.html')


def getUsers(request):
     return render(request,'signup.html')

def push(request):
    return render(request,'home.html')


def postsign(request):
    return render(request, 'signupUser.html')
def postSignupUser(request):
    email = request.POST.get('email')
    password = request.POST.get('pass')
    user = authe.create_user_with_email_and_password(email,password)
    uid = user['localId']
    data = {"email": email, "password":password}
    db.child('users').child(uid).set(data)
    return render(request, 'profileUser.html')

def postSignupDr(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    doctor=authe.create_user_with_email_and_password(email,password)
    did=doctor['localId']
    data={"email":email,"password":password}
    db.child('doctors').child(did).set(data)
    return render(request,'profileDoctor.html')

def signInDr(request):
    return render(request, 'signupDoctor.html')

def UpdateUser(request):
    import time
    from datetime import datetime, timezone
    import pytz

    idtoken = request.session['uid']
    print(idtoken)
    timestamps = db.child('UserProfile').get().val()
    print(timestamps)

    idtoken = request.session['uid']
    print(idtoken)
    timestamps = db.child('UserProfile').get().val()
    print(timestamps)
    for i in timestamps:
        name = []
        name1 = db.child('UserProfile').child(i).child('username').get().val()
        # name2=db.child('UserProfile').child(i).child('username').get().val()
        name.append(name1)
        address = []
        address1 = db.child('UserProfile').child(i).child('address1').get().val()
        address.append(address1)
        gender = []
        gender1 = db.child('UserProfile').child(i).child('gender').get().val()
        gender.append(gender1)
        phone = []
        phone1 = db.child('UserProfile').child(i).child('phone').get().val()
        phone.append(phone1)
        image = []
        image1 = db.child('UserProfile').child(i).child('image').get().val()
        image.append(image1)

        comb_lis = zip(name, address, gender, phone, image)

        tz = pytz.timezone('Asia/Kolkata')
        time_now = datetime.now(timezone.utc).astimezone(tz)
        millis = int(time.mktime(time_now.timetuple()))
        name = request.POST.get('uname')
        address = request.POST.get('uaddress')
        phone = request.POST.get('uphone')
        gender = request.POST.get('ugender')
        image = request.POST.get('uimage')
        data = {
            'uname': name,
            'uaddress': address,
            'uphone': phone,
            'ugender': gender,
            'uimage': image
        }
        print('timestamps:',timestamps)

        db.child('UserProfile').child(i).update(data)
        return render(request,'UpdateUser.html',{'comb_lis':comb_lis})

def UpdatedProfileUser(request):
    import datetime
    import time
    from datetime import datetime, timezone
    import pytz


    idtoken = request.session['uid']
    print(idtoken)
    timestamps = db.child('UserProfile').get().val()
    print(timestamps)
    lis_time = []
    name = []

    idtoken = request.session['uid']
    print(idtoken)
    timestamps = db.child('UserProfile').get().val()
    print(timestamps)
    for i in timestamps:
        name = []
        name1 = db.child('UserProfile').child(i).child('username').get().val()
        # name2=db.child('UserProfile').child(i).child('username').get().val()
        name.append(name1)
        address = []
        address1 = db.child('UserProfile').child(i).child('address1').get().val()
        address.append(address1)
        gender = []
        gender1 = db.child('UserProfile').child(i).child('gender').get().val()
        gender.append(gender1)
        phone = []
        phone1 = db.child('UserProfile').child(i).child('phone').get().val()
        phone.append(phone1)
        image = []
        image1 = db.child('UserProfile').child(i).child('image').get().val()
        image.append(image1)

        comb_lis = zip(name, address, gender, phone, image)

    return render(request,'ProfileViewUsers.html',{'comb_lis':comb_lis})

def userProfile(request):
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    try:
        user1=authe.sign_in_with_email_and_password(email,passw)
        print('user:',user1)
    except:
        message="Invalid Credential"
        return render(request,"Userlogin.html",{"message":message})
    return render(request,'ProfileChooseUser.html',{"e":email})

def doctorProfile(request):
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    try:
        doctor1=authe.sign_in_with_email_and_password(email,passw)
    except:
        message="Invalid Credential"

        return render(request,'Doctorlogin.html',{'message':message})
    return render(request,'profileChooseDr.html',{'e':email})



def logoutUser(request):

    authe.logout(request)
    return render(request,'Userlogin.html')



def createProfileUser(request):
    import time
    from datetime import datetime,timezone
    import pytz
    tz=pytz.timezone('Asia/Kolkata')
    time_now =datetime.now(timezone.utc).astimezone(tz)
    millis =int(time.mktime(time_now.timetuple()))
    timestamps=db.child('users').get().val()
    for i in timestamps:
        print(i)
    username =request.POST.get('username')
    address=request.POST.get('address1')
    phone=request.POST.get('phone')
    gender=request.POST.get('gender')
    image=request.POST.get('image')
    data = {
        'username' : username,
        'address1' : address,
        'phone':phone,
        'gender':gender,
        'image':image
    }
    name={
        'username':username
    }
    db.child('RequestAppointment').child(i).set(name)
    db.child('UserProfile').child(i).set(data)
   # db.child('UserProfile').child(a).child('reports').set(data)
    #name=db.child('UserProfile').child(a).child('details').child('name').get(idtoken).val()
    return render(request,'DeptChoose.html')
def createProfileDoctor(request):
    import time
    from datetime import datetime,timezone
    import pytz

    tz=pytz.timezone('Asia/Kolkata')
    time_now =datetime.now(timezone.utc).astimezone(tz)
    millis =int(time.mktime(time_now.timetuple()))
    timestamps = db.child('doctors').get().val()
    for i in timestamps:
        print(i)
    username =request.POST.get('username')
    address=request.POST.get('address')
    phone=request.POST.get('phone')
    speciality=request.POST.get('speciality')
    work=request.POST.get('work')
    year=request.POST.get('year')

    print(year)

    license=request.POST.get('license')
    data = {
        'username' : username,
        'phone':phone,
        'address':address,
        'speciality':speciality,
        'work':work,
        'year':year,
        'license':license
    }
    deptData={
        'speciality':speciality
    }
    name={
        'doctor':username
    }
    db.child('RequestAppointment').child(i).set(name)
    db.child('Dept').child(i).set(deptData)
    db.child('DoctorProfile').child(i).set(data)
    return render(request,'profileChooseDr.html')

def postDeptChooseUser(request):            #map integration
   # mapbox_access_token='pk.my_mapbox_access_token'
    import datetime
    timestamps = db.child('DoctorProfile').get().val()
    lis_time=[]
    for i in timestamps:
        lis_time.append(i)
        lis_time.sort(reverse=True)
        data=[]
    for i in timestamps:
        dat= db.child('DoctorProfile').child(i).get().val()
        data.append(dat)
        address=[]
        name=[]
        speciality=[]
    for i in timestamps:
            address1=db.child('DoctorProfile').child(i).child('address').get().val()
            address.append(address1)
    for i in timestamps:
            name1 = db.child('DoctorProfile').child(i).child('username').get().val()
            name.append(name1)
    for i in timestamps:
            speciality1 = db.child('DoctorProfile').child(i).child('speciality').get().val()
            speciality.append(speciality1)
    print("address",address)
    geolocator = Nominatim()
    try:
     #   loc = geolocator.geocode(address,timeout=10)
        loc=geolocator.geocode(address,timeout=10)
        print('loc:',loc)
        latitude = loc.latitude
        longitude = loc.longitude
        print(loc.latitude, loc.longitude)
    except GeocoderTimedOut as e:
       print("Error: geocode failed on input %s with message " % (address))
   #print(loc.latitude,loc.longitude)
    comb_lis=zip(name,speciality)
    return render(request,'map2.html',{'latitude':latitude,'longitude':longitude,'comb_lis':comb_lis})          #{'mapbox_access_token':mapbox_access_token})
def post_createDoctor(request):
    import time
    from datetime import datetime,timezone
    import pytz
    email = request.POST.get('email') #remove
    password = request.POST.get('password')  #remove
    user = authe.sign_in_with_email_and_password(email, password)  #remove
    tz=pytz.timezone('Asia/Kolkata')
    time_now =datetime.now(timezone.utc).astimezone(tz)
    millis =int(time.mktime(time_now.timetuple()))
    print("milli"+str(millis))
    did = user['localId']
    name=request.POST.get('name'),
    email =request.POST.get('email')
    password=request.POST.get('password'),

    idtoken =request.session['did']
    a=authe.get_account_info(idtoken)
    a=a['doctors']
    a=a[0]
    a=a['localId']
    print("info"+str(a))
    data={
        'email':email,
        'password':password
    }
   # db.child('users').child(a).child('doctorReports').child(millis).set(data)
   # name=db.child('users').child(did).child('details').child('name').get(idtoken).val()
    db.child('doctors').child(did).set(data)
    return render(request,'profileDoctor.html')



def Userlog(request):

    return render(request, 'Userlogin.html')

def postRegisterDoctor(request):
    return render(request,'profileChooseDr.html')
def chooseDept(request):
     email = request.POST.get('email')
     password = request.POST.get('password')
     return render(request, 'DeptChoose.html',{'e':email})


def Doctorlog(request):

    return render(request, 'Doctorlogin.html')



def ProfileViewUser(request):
    import datetime
   # idtoken = request.session['uid']
    #print(idtoken)
    timestamps = db.child('users').get().val()
    print(timestamps)
    lis_time = []
    for i in timestamps:
          print('i',i)
   #     lis_time.append(i)
    #    lis_time.sort(reverse=True)
    #print(lis_time)
    #data = []
    #for i in lis_time:
     # em=db.child('UserProfile').child(j).get().val()
      #data.append(em)
  #print(data)
    for i in timestamps:
        email=[]
        email1=db.child('users').child(i).child('email').get().val()
        email.append(email1)
        name=[]
        name1=db.child('UserProfile').child(i).child('username').get().val()
    #name2=db.child('UserProfile').child(i).child('username').get().val()
        name.append(name1)
        print(name)
        address=[]
        address1=db.child('UserProfile').child(i).child('address1').get().val()
        address.append(address1)
    #print(address)
        gender=[]
        gender1=db.child('UserProfile').child(i).child('gender').get().val()
        gender.append(gender1)
    #print(gender)
        phone=[]
        phone1=db.child('UserProfile').child(i).child('phone').get().val()
        phone.append(phone1)
    #print(phone)
        image=[]
        image1=db.child('UserProfile').child(i).child('image').get().val()
        image.append(image1)
    #print(image)
        comb_lis = zip(name,address,gender,phone,image,email)

    return render(request,'ProfileViewUsers.html',{'comb_lis':comb_lis})


def ProfileViewDoctor(request):
    import datetime
    speciality=request.POST.get('speciality')

   # idtoken = request.session['did']
   # print(idtoken)
    timestamps1=db.child('doctors').get().val()
    for i in timestamps1:
        email=[]
        email1=db.child('doctors').child(i).child('email').get().val()
        email.append(email1)
    timestamps = db.child('DoctorProfile').get().val()
    print(timestamps)
    lis_time = []
    for i in timestamps:
            print(i)
   #     lis_time.append(i)
    #    lis_time.sort(reverse=True)
    #print('lis_time:',lis_time)
    data = []
   # for j in lis_time:
    #    em = db.child('DoctorProfile').child(j).get().val()
     #   data.append(em)
    #print('data:',data)
    print('speciality:',db.child('DoctorProfile').child(i).child('speciality').get().val())
  #  if speciality==db.child('DoctorProfile').child(i).child('Speciality').get().val():
    for i in timestamps:
        name = []
        name1=db.child('DoctorProfile').child(i).child('username').get().val()
        name.append(name1)
        address = []
        address1 = db.child('DoctorProfile').child(i).child('address').get().val()
        address.append(address1)
        print(address)
        phone = []
        phone1 = db.child('DoctorProfile').child(i).child('phone').get().val()
        phone.append(phone1)
        print(phone)
        speciality = []
        speciality1 = db.child('DoctorProfile').child(i).child('speciality').get().val()
        speciality.append(speciality1)
        print(speciality)
        work = []
        work1 = db.child('DoctorProfile').child(i).child('work').get().val()
        work.append(work1)
        print(work)
        year = []
        year1 = db.child('DoctorProfile').child(i).child('year').get().val()
        year.append(year1)
        print(year)
        license = []
        license1 = db.child('DoctorProfile').child(i).child('license').get().val()
        license.append(license1)
        print(license)

    comb_lis = zip(name,address,license,phone,speciality,work,year,email)

    return render(request,'ProfileViewDr.html',{'comb_lis':comb_lis})



def ProfileViewDoctorOwn(request):
    import datetime
    speciality=request.POST.get('speciality')

  #  idtoken = request.session['uid']
   # print(idtoken)
    timestamps = db.child('DoctorProfile').get().val()
    print(timestamps)
    lis_time = []
    for i in timestamps:
            print(i)
    data = []
    print('speciality:',db.child('DoctorProfile').child(i).child('speciality').get().val())
  #  if speciality==db.child('DoctorProfile').child(i).child('Speciality').get().val():
    for i in timestamps:
        name = []
        name1=db.child('DoctorProfile').child(i).child('username').get().val()
        #name2 = db.child('DoctorProfile').child(i).child('username').get().val()
        name.append(name1)
        address = []
        address1 = db.child('DoctorProfile').child(i).child('address').get().val()
        address.append(address1)
        print(address)
        phone = []
        phone1 = db.child('DoctorProfile').child(i).child('phone').get().val()
        phone.append(phone1)
        print(phone)
        speciality = []
        speciality1 = db.child('DoctorProfile').child(i).child('speciality').get().val()
        speciality.append(speciality1)
        print(speciality)
        work = []
        work1 = db.child('DoctorProfile').child(i).child('work').get().val()
        work.append(work1)
        print(work)
        year = []
        year1 = db.child('DoctorProfile').child(i).child('year').get().val()
        year.append(year1)
        print(year)
        license = []
        license1 = db.child('DoctorProfile').child(i).child('license').get().val()
        license.append(license1)
        print(license)

        comb_lis = zip(name,address,license,phone,speciality,work,year)

        return render(request,'ProfileViewDrOwn.html',{'comb_lis':comb_lis})

def doctorSearch(request):
     return render(request,'doctorSearch.html')

def Timeslot(request):

    return render(request,'Timeslot2.html')
def TimeslotDoctor(request):
    return render(request,'TimeslotDoctor.html')


def postTimeslotDoctor(request):
    import time
    from datetime import datetime, timezone
    import pytz
    #idtoken = request.session['uid']
    #print(idtoken)
    timestamps = db.child('doctors').get().val()
    print(timestamps)
    lis_time = []
    for i in timestamps:
       print('i',i)

    tz = pytz.timezone('Asia/Kolkata')
    time_now = datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(time_now.timetuple()))
    date = request.POST.get('date')
    slot=request.POST.get('slot')
    data = {
        'date': date,
        'slot':slot
    }
    db.child('TimeslotDoctor').child(i).set(data)

    timestamps = db.child('UserProfile').get().val()
    print(timestamps)

    name=[]
    for i in timestamps:
        name1=db.child('UserProfile').child(i).child('username').get().val()
        name.append(name1)
   # print(name)
        address = []
        address1 = db.child('UserProfile').child(i).child('address1').get().val()
        address.append(address1)

        date=[]
        date1=db.child('RequestAppointment').child(i).child('date').get().val()
        date.append(date1)

        slots=[]
        slots1=db.child('RequestAppointment').child(i).child('slot').get().val()
        slots.append(slots1)

    comb=zip(name,address,date,slots)
    return render(request,'ViewAppointments.html',{'comb':comb})
def ratings1(request):
    import time
    from datetime import datetime, timezone
    import pytz
  #  idtoken = request.session['uid']
   # print(idtoken)
    timestamps = db.child('UserProfile').get().val()
    print(timestamps)
    for i in timestamps:
        name = []
        name1 = db.child('UserProfile').child(i).child('username').get().val()
        name.append(name1)
    #print(name)
    tz = pytz.timezone('Asia/Kolkata')
    time_now = datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(time_now.timetuple()))
    date = request.POST.get('date')
    slot = request.POST.get('slot')
    print(time)
   #db.child('RequestAppointment').child(millis).set(name)
    data = {
        'date': date,
        'slot':slot
    }
    db.child('RequestAppointment').child(i).set(data)
    return render(request,'ratings1.html')

def postratings(request):
    import time
    from datetime import datetime, timezone
    import pytz
    timestamps = db.child('DoctorProfile').get().val()
    print(timestamps)
    tz = pytz.timezone('Asia/Kolkata')
    time_now = datetime.now(timezone.utc).astimezone(tz)
    rating = request.POST.get('rating')
    comment = request.POST.get('comment')
    print(rating)
    print(comment)
    lis_time = []
    for i in timestamps:
        print('i', i)
    data={
         'comment':comment,
         'rating':rating
    }
    print(data)
    db.child('Ratings').child(i).set(data)
    return render(request,'welcome.html')
def confirm(request):
    return render(request,'confirm.html')