from django.urls import path

from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.allthread, name='allthread'),
    path('newthread', views.newthread, name='newthread'),
    path("like/<int:id>",views.like_post,name='like_post'),
    path("delete/<int:id>", views.delete_post, name='delete_post'),
    path("update", views.update_post, name="update_post"),
]