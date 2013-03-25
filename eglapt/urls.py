from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from django.views.generic.simple import direct_to_template

from tastypie.api import Api
from core.api import *

v1_api = Api(api_name='v1')
v1_api.register(GameResource())
v1_api.register(GameLevelResource())
v1_api.register(APTResource())
v1_api.register(UserResource())

urlpatterns = patterns('',
    url(r'^', include('core.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^api/', include(v1_api.urls)),
)

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
