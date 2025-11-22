from django.urls import path
from .import views
urlpatterns = [
path('indexadmin',views.indexadmin,name="indexadmin"),
path('userdetails',views.userdetails,name="userdetails"),
path('deliverydetails',views.deliverydetails,name="deliverydetails"),
path('employeedetails',views.employeedetails,name="employeedetails"),
path('additems',views.additems,name="additems"),
path('viewitems',views.viewitems,name="viewitems"),
path('edit',views.edit,name="edit"),
path('logadmin',views.logadmin,name="logadmin"),

]