from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
import home.views



urlpatterns = [
    path('admin', admin.site.urls),
    path('', home.views.index, name='home'),
    path('home/', include("home.urls")),
    path('certificates/', include("certificates.urls")),
    path('projects/', include("projects.urls")),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
