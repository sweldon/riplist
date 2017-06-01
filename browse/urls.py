from django.conf.urls import url
from browse import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^search_listings', views.search_listings, name='search_listings'),
    url(r'^get_address', views.get_address, name='get_address'),
    url(r'^materials/$', views.materials, name='materials'),
    url(r'^about/$', views.about, name='about'),
    url(r'^all_materials/$', views.all_materials, name='all_materials'),
    url(r'^all_equipment/$', views.all_equipment, name='all_equipment'),
    url(r'^all_sites/$', views.all_sites, name='all_sites'),

]