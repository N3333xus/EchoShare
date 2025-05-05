from django.contrib import admin
from django.urls import include, path

from django.conf.urls.static import static
from django.conf import settings

from echoshare_blog import views

urlpatterns = [
    path('admin/', 
    admin.site.urls),

    path('ckeditor/', 
    include("django_ckeditor_5.urls")),
    
    path('articles/<str:post_id>/', 
    views.post_detail, 
    name='post_detail'),

    path('articles/',
    views.articles,
    name='articles'),

    path('', views.home, 
    name='home'),
    
    path('about/',
    views.about,
    name='about'),
    
    path('privacy/', 
    views.privacy, 
    name='privacy'),
    
    path("image_upload/", 
    views.upload_file, 
    name="ck_editor_5_upload_file"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


