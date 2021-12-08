from django.urls import path

from . import views

app_name = 'error'

urlpatterns = [
    path('not_found/', views.not_found, name="not_found"),
]
