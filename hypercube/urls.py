from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from scraper import views as ebooks_views

urlpatterns = [
    url(r'^$', ebooks_views.home, name='home'),
    url(r'^search/$', ebooks_views.search, name='search'),
    url(r'^about/$', ebooks_views.about, name='about'),
    url(r'^policy/$', ebooks_views.policy, name='policy'),
    url(r'^contact/$', ebooks_views.contact_us, name='contact'),

    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
