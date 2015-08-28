from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'odoomatrix.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^matrix/', include('matrix.urls'), name='matrix'),
    url(r'^$', 'matrix.views.v_view_last_matrix')
)
