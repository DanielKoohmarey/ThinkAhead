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
    #http://garmoncheg.blogspot.com/2012/07/django-resetting-passwords-with.html
    url(r'^password/reset/$', 
            'django.contrib.auth.views.password_reset', 
            {'post_reset_redirect' : '/password/reset/done/'},
            name="password_reset"),
        (r'^password/reset/done/$',
            'django.contrib.auth.views.password_reset_done'),
        (r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
            'django.contrib.auth.views.password_reset_confirm', 
            {'post_reset_redirect' : '/password/done/'}),
        (r'^password/done/$', 
            'django.contrib.auth.views.password_reset_complete'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', splash),
    url(r'^home/$', splash),
    url(r'^logout/$', userLogout),
    url(r'^registration/$',userRegistration),
    url(r'^dashboard/$', dashboard),
    url(r'^profile/$', updateProfile),
    url(r'^autocompleteCourse', autocompleteCourse),

)
