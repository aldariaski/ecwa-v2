from django.urls import path
from .views import *

app_name = 'comment'

urlpatterns = [
    path('detail/<int:id>', detail_post, name='detail_post'),
    path("comment/<int:id>", comment_post,name='comment_post'),
    path("comment/del/<int:id>", del_com,name='del_com'),
    path("comment/del1/<int:id>", del1_com,name='del1_com')
]