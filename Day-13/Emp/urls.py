from django.urls import path
from Emp import views

urlpatterns = [
       
    path('',views.home,name="hm"),
    path('abt/',views.about,name="ab"),
    path('contact/',views.contact,name="co"),
    path('login/',views.login,name="lg"),
    path('register/',views.registration,name="rg"),
 	path('actions/',views.crud,name="na"),
 	path('delt/<int:id>',views.deletedata,name="delete"),
 	path('df/',views.dform,name="dff"),
 	path('shw/',views.showinfo,name="sh"),
 	path('infodelete/<int:id>',views.infodelete,name="infodelete"),
 	# path('infoedit/<int:id>',views.edit,name="infoedit"),
 	path('ed/<int:si>/',views.userupdate,name="ue"),
]