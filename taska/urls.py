from django.urls import path
from . import views
urlpatterns =[
    path('login/',views.index,name='index'),
    path('login/task.html/',views.index1,name='index1'),
    path('login/signup.html/',views.index2,name='index2'),
    path('login/signup.html/login/',views.index1,name='index1'),
]