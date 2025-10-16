from django.urls import path
from .import views
urlpatterns = [
path('',views.index,name="index"),
path('userlog',views.userlog,name="userlog"),
path('userreg',views.userreg,name="userreg"),
path('userhome',views.userhome,name="userhome"),
path('emplog',views.emplog,name="emplog"),
path('empreg',views.empreg,name="empreg"),
path('emphome',views.emphome,name="emphome"),
path('plist',views.plist,name="plist"),
path('pdetails',views.pdetails,name="pdetails"),
path('bdetails',views.bdetails,name="bdetails"),
path('profile1',views.profile1,name="profile1"),
path('cartview',views.cartview,name="cartview"),
path('about',views.about,name="about"),

]