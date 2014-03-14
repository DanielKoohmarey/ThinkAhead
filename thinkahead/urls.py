from django.conf.urls import patterns, include, url
from darsplus.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thinkahead.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^/$', splash),
    url(r'^home/$', splash),
    url(r'^logout/$', userLogout),
    url(r'^registration/$',userRegistration),
    url(r'^dashboard/$', dashboard),
)
