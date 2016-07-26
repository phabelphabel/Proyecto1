from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',

    #url(r'^user/responsable/$',responsable_view),
    #url(r'^user/listar_responsable/$',listar_responsable_view),
    #url(r'^user/carrera/$',carrera_view),
    #url(r'^user/listar_carrera/$',listar_carrera_view),
    #url(r'^user/modi_responsables/$',modi_responsables_view),
    #url(r'^user/modificar_responsable/$',modificar_responsable_view),
    url(r'^user/encargado/$',encargado_view),
    url(r'^user/registro_carreras/$',carrera_view),
    url(r'^user/listar_carreras/$',listar_carrera_view),
    url(r'^user/editar_carreras/(?P<carrera_id>\d+)/$',editar_carreras_view),
    url(r'^user/registro_proveedor/$',proveedor_view),
    url(r'^user/listar_proveedor/$',listar_proveedor_view),
    url(r'^user/editar_proveedor/(?P<proveedor_id>\d+)/$',editar_proveedor_view),
    url(r'^user/registrar_grupo_contable/$',grupo_contable_view),
    url(r'^user/registrar_activo/$',activo_view),
)