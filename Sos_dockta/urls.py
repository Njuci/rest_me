from  django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include


api1="apihopital/"
ap1="http://127.0.0.1:8000/apihopital/ApiTousleshopitaux/"
urlpatterns = [
    path('admin/', admin.site.urls),
    path(api1,include('djoser.urls')),
    path(api1,include('djoser.urls.authtoken')),
    path("",include("SOS.urls")),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)