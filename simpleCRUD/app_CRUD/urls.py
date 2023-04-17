from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('addMember/',views.addMember,name='add_Member'),
    path('addrec/',views.addrec,name="addrec")
]
