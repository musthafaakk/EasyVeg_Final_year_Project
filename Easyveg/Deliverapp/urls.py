from django.urls import path
from .import views
urlpatterns = [
    path('deliverylog',views.deliverylog,name="deliverylog"),
    path('deliveryreg',views.deliveryreg,name="deliveryreg"),
    path('deliveryhome',views.deliveryhome,name="deliveryhome"),
    path('about',views.about,name="about"),
    path('profile1',views.profile1,name="profile1"),
]