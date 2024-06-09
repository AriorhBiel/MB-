from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('note/date', views.date_get),
    path('note/date/post', views.date_post),
    path('note/date/put', views.date_put),
    path('note/date/del', views.date_del),
    path('note/record', views.rec_get),
    path('note/record/post', views.rec_post),
    path('note/record/put', views.rec_put),
    path('note/record/del', views.rec_del)
]
