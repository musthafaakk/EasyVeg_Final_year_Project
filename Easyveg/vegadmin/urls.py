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
path('eapprove<int:aid>',views.eapprove,name="eapprove"),
path('ereject<int:aid>',views.ereject,name="ereject"),
path('dapprove<int:did>',views.dapprove,name="dapprove"),
path('dreject<int:did>',views.dreject,name="dreject"),
path('dpedit<int:aid>',views.dpedit,name="dpedit"),
path('fdel<int:aid>',views.fdel,name="fdel"),
]