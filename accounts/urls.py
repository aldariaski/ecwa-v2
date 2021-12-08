from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/<str:username>/', views.readProfile, name="readProfile"),
    path('update/', views.updateProfile, name="updateProfile"),
    path('delete/', views.deleteProfile, name="deleteProfile"),
]
