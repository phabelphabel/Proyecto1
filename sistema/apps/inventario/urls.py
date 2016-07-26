from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',

    url(r'^user/accesorio/$',accesorio_view),

)