from django.conf.urls import include, url, patterns
from .views import index, index2

urlpatterns = patterns('',
	url(r'^$', 'apps.inicio.views.index'),
	url(r'^index2/$', index2.as_view()),
)