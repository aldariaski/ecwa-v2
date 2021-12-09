from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as django_logout
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from main.models import Profile
from jurnal.models import Journal
from django.core.serializers.json import DjangoJSONEncoder
import datetime

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        username = data.get("username")
        password = data.get("password")
        testUser = None
        try:
            testUser = User.objects.get(username=data['username'])
        except:
            pass
        if (testUser != None):
            return JsonResponse({}, status = 409)
        user = User.objects.create_user(username=username, password=password)
        privateJournal = Journal.objects.create(usernamezz = username, totals = 0, recordtotals = 0)
        user.profile.name = data.get("name")
        user.profile.birth_date = datetime.date(data.get("year"), data.get("month"), data.get("day"))
        user.profile.gender = data.get("gender")
        user.profile.phone_number = data.get("phone_number")
        user.profile.address = "Update profile to insert this"
        user.profile.occupation = "Update profile to insert this"
        user.profile.description = "This is my description!!"
        user.profile.role = "User"
        user.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        return JsonResponse({}, status = 200)
    return render(request, 'register/views.html')
