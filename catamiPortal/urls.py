from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'catamiPortal.views.home', name='home'),
    # url(r'^catamiPortal/', include('catamiPortal.foo.urls')),
    url(r'^Force/$','Force.views.index'),

    #to hide the database name
    url(r'^main/$','Force.views.index'),
    
    url(r'^main/auvdeployments/$', 'Force.views.auvdeployments'),

    url(r'Force/', include('Force.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
