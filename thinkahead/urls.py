from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView, RedirectView
from darsplus.views import *
from django.contrib import admin
admin.autodiscover()

class TextPlainView(TemplateView):
  def render_to_response(self, context, **kwargs):
    return super(TextPlainView, self).render_to_response(
      context, content_type='text/plain', **kwargs)
      
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thinkahead.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', splash),
    url(r'^home/$', splash),
    url(r'^logout/$', userLogout),
    url(r'^registration/$',userRegistration),
    url(r'^dashboard/$', dashboard),
    url(r'^profile/$', updateProfile),
)
