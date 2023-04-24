from django.urls import path
from . import views

urlpatterns=[path('',views.login1, name='login'),
             path('login2',views.login2, name='login2'),
             path('option',views.option, name='option'),
             path('student', views.student, name="student"),
             path('newenrollment',views.newenrollment, name='newenrollment'),
             path('bookingConfirmation',views.bookingConfirmation, name='bookingConfirmation'),
             path('feesrecipt',views.feesrecipt, name='feesrecipt'),
             path('reciptform',views.reciptform, name='reciptform'),
             path('recipt',views.recipt, name='recipt'),
             path('ss',views.ss,name='ss'),
             path('courses',views.courses,name='courses'),
             ]