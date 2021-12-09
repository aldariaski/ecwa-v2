from django.shortcuts import render, redirect
from django.urls import reverse
from . import forms
from .models import Question

# Create your views here.

def home(request):
    context= {
        'question_list':Question.objects.all()
    }
    print(context)
    return render(request, 'faq/home.html', context)

def create_faq(request):
    form = forms.Question()
    context = {'form':form}
    if request.method == "POST":
        print(request)
        form = forms.Question(request.POST)
        if form.is_valid():
            question = Question(pesan=form.cleaned_data['pertanyaan'])
            question.save()
            return redirect(reverse("faq:home"))
    return render(request, 'faq/create-faq.html', context)

def update_faq(request):
    context = {
        "id_question" : request.POST["id_question"]
    }
    if request.method == "POST":
        print(request.POST)
    return render(request, 'faq/update-faq.html', context)

def update_faq_2(request):
    """Update FAQ happens here"""
    context = {}
    if request.method == "POST":
        id = request.POST["id_question"]
        question = request.POST["question"]
        obj_q = Question.objects.get(id=id)
        obj_q.pesan = question
        obj_q.save()
    return redirect(reverse("faq:home"))

def delete_faq(request):
    id = request.GET['id']
    item = Question.objects.get(id=id)
    print(item)
    item.delete()
    return redirect(reverse("faq:home"))
