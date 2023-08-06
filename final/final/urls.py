from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 
from django.contrib import admin
from django.urls import path
from final import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('upload', views.upload, name='upload'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('FAQ/', views.FAQ, name='FAQ'),
    path('Term/', views.Term, name='Term'),
    
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL2, document_root=settings.MEDIA_ROOT2)