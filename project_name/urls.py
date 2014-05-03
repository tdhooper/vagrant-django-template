from django.conf.urls import patterns, include, url
from django.contrib import admin
import urltools

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += urltools.get_app_urls()