from django.urls import path
from hu import views

urlpatterns=[
	path('',views.home,name='hm'),
     path('abt/',views.about,name='abt'),
     path('cnt/',views.contact,name='ct'),
     path('lgn/',views.login,name='lg'),
     path('reg/',views.registration,name='rg'),
     path('crud/',views.action,name='tr'),
     path('dlt/<int:r>/',views.delte,name="dl"),
]