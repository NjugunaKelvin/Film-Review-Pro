
# images 
from django.conf.urls.static import static
from . import settings


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

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)