from django.conf.urls import url
from browse import views

urlpatterns = [

    url(r'^$', views.index, name='index'),

]