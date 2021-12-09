from django.shortcuts import render

# Create your views here.
def not_found(request):
    return render(request,"error/not_found.html")