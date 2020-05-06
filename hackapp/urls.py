from django.urls import path,include
from .import views
urlpatterns = [
    path('', views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),

    path('signin/',views.postsign,name='signin'),

    path('oauth/',include('social_django.urls',namespace='social')),
    path('google_auth/', include('google_auth.urls')),

    path('Userlog/',views.Userlog,name='Userlog'),
    path('Doctorlog/',views.Doctorlog,name='Doctorlog'),
    path('logoutUser/',views.logoutUser,name='logoutUser'),
    path('UpdateUser/',views.UpdateUser,name='UpdateUser'),
    path('UpdatedProfileUser/',views.UpdatedProfileUser,name='UpdatedProfileUser'),

    path('postSignupUser/',views.postSignupUser,name="postSignupUser"),
    path('postSignupDr/',views.postSignupDr,name="postSignupDr"),
    path('postRegisterDoctor/',views.postRegisterDoctor,name='postRegisterDoctor'),
    path('createProfileUser/', views.createProfileUser, name='createProfileUser'),
    path('createProfileDoctor/',views.createProfileDoctor,name='createProfileDoctor'),
    path('postDeptChooseUser/',views.postDeptChooseUser,name='postDeptChooseUser'),  #map
    path('userProfile/',views.userProfile,name='userProfile'),
    path('doctorProfile/',views.doctorProfile,name='doctorProfile'),




    path('signinDr/',views.signInDr,name="signinDr"),
    path('post_createDoctor/',views.post_createDoctor,name='post_createDoctor'),

    path('check/',views.check,name="check"),
    path('getUsers/',views.getUsers,name='getUsers'),
    path('push/',views.push,name='push'),


    path('ProfileViewUser/',views.ProfileViewUser,name='ProfileViewUser'),
    path('ProfileViewDoctor/',views.ProfileViewDoctor,name='ProfileViewDoctor'),
    path('ProfileViewDoctorOwn/',views.ProfileViewDoctorOwn,name='ProfileViewDoctorOwn'),


    #path('doctorSearch/',views.doctorSearch,name='doctorSearch')


   # path('ratings/', include('star_ratings.urls', namespace='ratings')),

    path('Timeslot/',views.Timeslot,name='Timeslot'),
    path('TimeslotDoctor/',views.TimeslotDoctor,name='TimeslotDoctor'),
    path('postTimeslotDoctor/',views.postTimeslotDoctor,name='postTimeslotDoctor'),

    path('ratings1/',views.ratings1,name='ratings1'),
    path('postratings/',views.postratings,name='postrating'),
    path('confirm/',views.confirm,name='confirm')
]