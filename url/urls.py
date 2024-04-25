from . import views
from django.urls import path

urlpatterns=[
    path('',views.signin,name='login'),
    path('enter',views.enter,name='enter'),
    path('register',views.signup,name='register'),
    path('submit',views.submit,name='submit'),
    path('home',views.home,name='home'),
    path('add',views.add,name='add'),
    path('view',views.view,name='view')
]