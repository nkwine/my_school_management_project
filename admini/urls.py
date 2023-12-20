from . import views
from django.urls import path

urlpatterns =[
    path('home',views.home, name='home'),
    path('mteachers',views.mteachers,name='mteachers'),
    path('mstudents',views.mstudents,name='mstudents'),
    path('mdos',views.mdos,name='mdos'),
    path('madministrators',views.madministrators,name='madministrators'),
    path('msecretary',views.msecretary,name='msecretary'),
    path('mbursar',views.mbursar,name='mbursar'),
    path('msupportstaff',views.msupportstaff,name='msupportstaff'),
    path('teacher_registration', views.teacher_registration, name='teacherreg'),
    path('administrator_registration', views.administrator_registration, name='administrator_registration'),
    path('secretary_registration', views.secretary_registration, name='secretary_registration'),
    path('bursar_registration', views.bursar_registration, name='bursary_registration'),
    path('dos_registration', views.dos_registration, name='dos_registration')
]