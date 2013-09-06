from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myweb.views.home', name='home'),
    # url(r'^myweb/', include('myweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', include('home.urls')),
    url(r'^$', 'home.views.test', name='test'),
    url(r'^CSresume$','home.views.pdf_view_cs',name='pdf_view_cs'),
    url(r'^EEresume$','home.views.pdf_view_ee',name='pdf_view_ee'),
    
)
