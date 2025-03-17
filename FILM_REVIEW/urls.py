
# images 
from django.conf.urls.static import static
from django.conf import settings


from django.contrib import admin
from django.urls import path,include
from movies import views as movieViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', movieViews.home, name='home'),
    path('about/',movieViews.about),
    path('news/',include('news.urls')),
    path('movie/',include('movies.urls')),
    path('accounts/',include('accounts.urls')),
]

# urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])