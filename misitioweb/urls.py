from django.conf.urls import patterns, include, url
from django.contrib import admin
 
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'misitioweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^index/', 'grafos.views.index'),
	url(r'^sobre/', 'grafos.views.sobre'),
	url(r'^$', 'grafos.views.index'),
	url(r'^inicio/', 'grafos.views.index'),
	url(r'^explorar/', 'grafos.views.explorar'),
	url(r'^search/', 'grafos.views.search'),
	url(r'^ingresar-nodo/', 'grafos.views.ingresar-nodo' , name='ingresar-nodo'),
	url(r'^pruebas/', 'grafos.views.pruebas'),
	url(r'^registro/', 'grafos.views.registro'),
	url(r'^hello_pdf/','grafos.views.hello_pdf')
)
