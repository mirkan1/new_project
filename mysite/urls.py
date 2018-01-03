from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views
from shorterner.views import URLRedirectView, HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^accounts/main/$', views.login, name='main'),
    url(r'', include('blog.urls')),
    url(r'^urlshort/$', HomeView.as_view()),
    url(r'^(?P<shortcode>[\w-]+)/$', URLRedirectView.as_view(), name='sc'),
]