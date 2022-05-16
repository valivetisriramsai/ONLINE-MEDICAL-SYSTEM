import re
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse

# Create your views here.
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import user_serializer,login_serializer,docs_serializer,appointment_serializer
from rest_framework import status
from users.models  import *

@api_view(['GET'])
def current_users(request):
    users=User.objects.all();
    users_json=user_serializer(users,many=True);
    print(users_json)
    return Response(users_json.data)
    
    
@api_view(['POST'])
def add_users(request):
    user=request.data
    print(user)
    users_json=None
    if user:
        User.objects.create(username=user['name'],email=user['email'])
        User.save
        u=User.objects.get(username=user['name'])
        users_json=user_serializer(u,many=False)
    
            
    return Response(users_json.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def login_auth(request):
    user=request.data
    login_user=User.objects.get(email=user['email'])
    print(login_user)
    if login_user:
        u=user_serializer(login_user,many=False)
        return Response(u.data,status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getDoctors(request):
    docs=doctors.objects.all()
    docs_json=docs_serializer(docs,many=True)
    return Response(docs_json.data,status=status.HTTP_200_OK)


@api_view(['GET'])
def get_appointments(request,id):
    user_appointments=appointments.objects.filter(user=id);
    json=appointment_serializer(user_appointments,many=True);
    print(json)
    return Response(json.data)

@api_view(['GET'])
def get_appointment(request,id):
    appointment=appointments.objects.get(id=id);
    json=appointment_serializer(appointment,many=False)
    return Response(json.data)

@api_view(['GET'])
def get_doctor(request,id):
    doctor=doctors.objects.get(id=id);
    json=docs_serializer(doctor,many=False);
    return Response(json.data)

@api_view(['DELETE'])
def delete_appointment(request,id):
    print(id)
    appointments.objects.get(id=id).delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def add_appointment(request):
    data=request.data
    app=doctors.objects.get(id=data['doctor_id'])
    u=User.objects.get(id=data['user_id'])
    appointments.objects.create(user=u,doctor=app,time=data['appointment_date'])
    return Response(status=status.HTTP_200_OK)
    

    
        
    