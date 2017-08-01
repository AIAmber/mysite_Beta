"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import cmdb.views
import lvhang.views
import blog.views
from mysite import settings
from django.views import static

urlpatterns = [
    url(r'^$', blog.views.get_blogs, name='blog_get_blogs'),
    url(r'^detail/(\d+)/$',blog.views.get_detail, name = 'blog_get_detail'),
    url(r'^admin/', admin.site.urls),
    url(r'^tangshi/$', cmdb.views.tangshi),
    url(r'^lvhang/$',lvhang.views.lvhang),
    url(r'^login/$', lvhang.views.login),
    url(r'^time/$', cmdb.views.time),
    url(r'^time/(\d{1,2})/$', cmdb.views.hours_ahead),
    url(r'^demo/$', cmdb.views.demo),
    url(r'^test/$', cmdb.views.ptmpdb_list),
    url(r'^photo/$', cmdb.views.photo),

    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
]
