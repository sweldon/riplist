from django.conf.urls import url
from login import views

urlpatterns = [

    url(r'^$', views.login_page, name='login_page'),
    url(r'^logout/', views.logout_page, name='logout_page'),
    url(r'^register/', views.register, name='register'),

]