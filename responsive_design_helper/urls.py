from django.conf.urls.defaults import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^(?P<uri>.*)responsive/$', views.ResponsiveTestView.as_view()),
)
