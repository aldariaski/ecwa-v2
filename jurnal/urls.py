from django.urls import path

from . import views

app_name = 'jurnal'

urlpatterns = [
    path('', views.jurnal_front, name='jurnal_front'),
    path('add-record/', views.add_record, name='add_record'),
    path('update-record/', views.update_record, name='update_record'),
    path('delete-record/<int:id>/', views.delete_record, name='delete_record'),
    path('drop-record/', views.drop_record, name='drop_record'),
]
