from webbrowser import get
from django.urls import path,include

from . import views
urlpatterns =[
    path('',views.current_users,name='users'),
    path('add',views.add_users,name='add'),
    path('login_auth',views.login_auth,name='auth'),
    path('doctors',views.getDoctors,name='doctors'),
    path('appointments/<id>',views.get_appointments,name='appointments'),
    path('appointment/<id>',views.get_appointment,name='appointment'),
    path('doctors/<id>',views.get_doctor,name='doctors'),
    path('delete/<id>',views.delete_appointment,name='delete'),
    path('add/appointment',views.add_appointment,name='add_app')
]