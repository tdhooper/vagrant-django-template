from django.conf.urls import patterns, include, url
from django.contrib import admin
import apptools

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += apptools.get_app_urls()