
"""eticketV1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from eticketV1.apps.views import login, inicio, menu, multa, formulario, mulvehiculo, formulIma, menu1, menu2, menu3, menu4, menu5
admin.autodiscover()
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$','eticketV1.apps.logueo.views.login'),
    url(r'^paso2/',inicio),
    url(r'^paso1/',login),
    url(r'^paso3/',menu),
    url(r'^paso4/',multa),
    url(r'^paso6/',formulario),
    url(r'^paso7/',formulIma),
    url(r'^paso5/',mulvehiculo),
    url(r'^paso8/',menu1),
    url(r'^paso9/',menu2),
    url(r'^paso10/',menu3),
    url(r'^paso11/',menu4),
    url(r'^paso12/',menu5),

)
