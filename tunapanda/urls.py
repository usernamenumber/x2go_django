from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tunapanda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^/?$', 'tunapanda.views.index'),
    url(r'^admin/', include(admin.site.urls)),
)
