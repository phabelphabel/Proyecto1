from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sistema.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^', include('sistema.apps.principal.urls')),
    url(r'^', include('sistema.apps.usuario.urls')),
    url(r'^', include('sistema.apps.encargado.urls')),
    url(r'^', include('sistema.apps.inventario.urls')),
)
