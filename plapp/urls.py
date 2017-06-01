"""plapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponseRedirect
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'browse.views.error404'
handler500 = 'browse.views.error500'


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', lambda r: HttpResponseRedirect('browse/')),
    url(r'^login/', include('login.urls')),
    url(r'^browse/', include('browse.urls')),
    url(r'^create_listing/', include('list.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)