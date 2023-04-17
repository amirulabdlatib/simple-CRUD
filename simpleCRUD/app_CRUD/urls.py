from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('addMember/',views.addMember,name='add_Member'),
    path('addrec/',views.addrec,name="addrec"),
    path('delete/<int:id>/',views.deleterec,name='deleterec'),
    path('update/<int:id>/',views.update,name="update"),
    path('update/updaterec/<int:id>/',views.updaterec,name="updaterec"),

]
