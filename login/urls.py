from django.conf.urls import url
from login import views
from django.contrib.auth.views import password_reset_confirm, password_reset_complete

urlpatterns = [

    url(r'^$', views.login_page, name='login_page'),
    url(r'^logout/', views.logout_page, name='logout_page'),
    url(r'^register/', views.register, name='register'),
    url(r'^recover$', views.recover, name='recover'),
    # url(r'^recover/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^recover/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', views.passwordresetpage, name='passwordresetpage'),
    url(r'^accounts/password/done/$', views.password_reset_complete, name='password_reset_complete'),

]