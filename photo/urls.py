from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'photo'
urlpatterns = [
    path('upload/', views.fileUpload, name='upload'),
    path('img_info/<int:id>/', views.img_info, name='img_info'),
    path('photo/favorit/<int:id>/', views.favorites, name='favorites'),
    path('photo/favorit/', views.favorites_view, name='get_favorites'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
