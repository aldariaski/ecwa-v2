from django.urls import path

from . import views

app_name = 'faq'

urlpatterns = [
    path('', views.home, name='home'),
    path('update2/', views.update_faq_2, name='update_faq_2'),
    path('update/', views.update_faq, name='update_faq'),
    path('create/', views.create_faq, name='create_faq'),
    path('delete/', views.delete_faq, name='delete_faq'),
]