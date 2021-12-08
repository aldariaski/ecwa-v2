from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from main.models import Profile
from jurnal.models import Journal
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url="/accounts/login")
def readProfile(request, username):
    try:
        userProfile = User.objects.get(username = username)
    except:
        return redirect("error:not_found")        
    context = {
        "userProfile" : userProfile,
    }
    return render(request,"accounts/read_profile.html",context)

@csrf_exempt    
@login_required(login_url="/accounts/login")
def updateProfile(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user = request.user
        user.profile.name = data.get("name")
        user.profile.gender = data.get("gender")
        user.profile.phone_number = data.get("phone_number")
        user.profile.address = data.get("address")
        user.profile.occupation = data.get("occupation")
        user.profile.description = data.get("description")
        user.save()
        return JsonResponse({}, status = 200)
    # context = {
    #     "berita" : berita,
    # }
    # return render(request,"DetailPost_view.html",context)
    return render(request,"accounts/update_profile.html")

@csrf_exempt  
@login_required(login_url="/accounts/login")
def deleteProfile(request):
    if request.method == 'POST':
        user = request.user
        jurnal = Journal.objects.get(usernamezz=user.username)
        jurnal.delete()
        user.delete()
        return JsonResponse({}, status = 200)
    # context = {
    #     "berita" : berita,
    # }
    # return render(request,"DetailPost_view.html",context)
    return render(request,"accounts/read_profile.html")
