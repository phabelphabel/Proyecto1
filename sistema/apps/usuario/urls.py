from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',

    url(r'^user/registro/$',registro_view),
    url(r'^login/$',login_view),
    url(r'^logout/$',logout_view),
    url(r'^user/perfil/$',perfil_view),
    url(r'^user/active/$',user_active_view),
    url(r'^user/listar_usuario/$',listar_usuario_view),
    url(r'^user/editar_usuario/(?P<id_user>\d+)/$',editar_usuario_view),
    #url(r'^user/eliminar_personal/(?P<id>\d+)/$',eliminar_personal_view),
    url(r'^user/registro_personal/$',registro_personal_view),
    url(r'^user/listar_personal/$',listar_personal_view),
    url(r'^user/tipo/$',tipo_view),
    url(r'^user/administrador/$',administrador_view),
    url(r'^user/encargado/$',encargado_view),
    url(r'^user/editar_personal/(?P<personal_id>\d+)/$',editar_personal_view),
    url(r'^user/buscar_personal/$',buscar_personal_view),
    url(r'^user/crear_reporte_personal/$',crear_reporte_personal_view),

    #url(r'^user/active/$',user_active_view),
    #url(r'^user/ver_fusuario/$',ver_fusuario_view),
)