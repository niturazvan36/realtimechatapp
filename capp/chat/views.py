from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.views import View
from .forms import UserCreation
from django.contrib import messages
from .models import Chat,ChatRoom
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()
def home(req):

    return render(req, 'home.html', {})


def register(req):
    form = UserCreation(req.POST or None)
    if req.method == "POST" and form.is_valid():
        username = form.cleaned_data['username']
        form.save()
        return redirect('login')
    return render(req,'register.html',{'form':form})

class Room(LoginRequiredMixin, View):
     def get(self,request,room_name):
        Chat.objects.all().order_by('-id')
        room = ChatRoom.objects.filter(name=room_name).first()
        chats = []

        if room:
            chats = Chat.objects.filter(room=room)
        else:
            room = ChatRoom(name=room_name)
            room.save()
        Chat.objects.all().order_by('-id')
        return render(request,'room.html', {
        'room_name': room_name,
            'chats':chats
    })


def get_data(request, *args):
    data={
        "sales":100,
        "customers":10,
    }
    return JsonResponse(data)

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count=User.objects.all().count()
        default_items= [5, qs_count,1,qs_count+10]
        data = {
            "default":default_items
        }
        return Response(data)