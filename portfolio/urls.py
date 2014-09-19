from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'website.views.home', name='home'),
    url(r'^about_me/$', 'website.views.about_me', name='about_me'),
    url(r'^projects/$', 'website.views.projects', name='projects'),
    url(r'^comments/$', 'website.views.comments', name='comments'),
    url(r'^email/$', 'website.views.email', name='email'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)