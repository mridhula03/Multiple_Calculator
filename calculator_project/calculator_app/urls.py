from . import views
from django.urls import path

urlpatterns= [
    path('',views.frontpage),
     path('frontpage', views.frontpage),
    path('index', views.index),
    path('simpleinterest', views.simpleinterest),
    path('compoundinterest', views.compoundinterest),
    path('age', views.age),
    path('fatp', views.fatp),
    path('percentage', views.percentage),
    path('cgpa', views.cgpa),
    path('hour', views.hour),
    path('loan', views.loan),
    path('salary', views.salary),
]