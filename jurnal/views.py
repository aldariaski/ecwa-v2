from django.core.checks import messages
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as django_logout
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from .models import Record, Journal
from django.contrib.auth.decorators import login_required

@login_required(login_url="/account/login")
def jurnal_front(request):
    username = request.user.username
    print(username)
    journal = Journal.objects.get(usernamezz = username)
    context = {
        "recordiams" : Record.objects.filter(journal__pk = journal.id),
        "uzername" : username,
        "sumazi" : journal.totals
    }
    # Record.objects.filter(journal=journal)
    return render(request, 'jurnal/jurnalfront.html', context)

@login_required(login_url="/account/login")
def add_record(request):
    if request.method == 'POST':
        jumlah = (int)(request.POST["jumlah"])
        if (int)(jumlah) < 0:
            jumlah = -1 * jumlah
        tipe = request.POST["tipe"]
        journalz = request.user.username
        journale = Journal.objects.get(usernamezz = journalz)
        idz = journale.recordtotals + 1
        journale.recordtotals += 1
        if tipe == "C":
            journale.totals -= (int)(jumlah)
        else:
            journale.totals += (int)(jumlah)
        journale.save()
        new_record = Record.objects.create(recordid = idz, typezz = tipe, values = jumlah, journal = journale)
        new_record.save()
        return redirect('jurnal:jurnal_front')
    return render(request, 'jurnal/formAdd.html')

@login_required(login_url="/account/login")
def update_record(request):
    if request.method == 'POST':
        journalz = request.user.username
        journale = Journal.objects.get(usernamezz = journalz)
        recordo = Record.objects.get(recordid = request.POST['idz'], journal = journale)
        temp = 0
        jumlah = (int)(request.POST["jumlah"])
        if (int)(jumlah) < 0:
            jumlah = -1 * jumlah
        if recordo.typezz == "C":
            if request.POST['tipe'] == "C":
                temp = -1 * ((int)(jumlah) - recordo.values)
            else:
                temp = (int)(jumlah) + recordo.values
        else:
            if request.POST['tipe'] == "C":
                temp = -1 * ((int)(jumlah) + recordo.values)
            else:
                temp = (int)(jumlah) - recordo.values
        journale.totals += temp
        recordo.typezz = request.POST.get('tipe', False)
        recordo.values = request.POST.get('jumlah', False)
        recordo.save()
        journale.save()
        return redirect('jurnal:jurnal_front')
    return render(request, 'jurnal/formUpdate.html')


@login_required(login_url="/account/login")
def delete_record(request, id):
    if request.method == 'POST':
        print(id)
        journalz = request.user.username
        journale = Journal.objects.get(usernamezz = journalz)
        recorde = Record.objects.get(recordid = id, journal = journale)
        val = recorde.values
        print(val)
        if recorde.typezz == "C":
            journale.totals += val
        else:
            journale.totals -= val
        journale.recordtotals -= 1
        journale.save()
        recorde.delete()
    return redirect('jurnal:jurnal_front')


@login_required(login_url="/account/login")
def drop_record(request):
    if request.method == 'POST':
        username = request.user.username
        print(username)
        journal = Journal.objects.get(usernamezz = username)
        records = Record.objects.filter(journal__pk = journal.id)
        records.delete()
        journal.totals = 0
        journal.recordtotals = 0
        journal.save()
        return redirect('jurnal:jurnal_front')
    return render(request, 'jurnal/formDrop.html')