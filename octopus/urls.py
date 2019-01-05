from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('words/', include('word_cloud.urls')),
    path('', include('word_cloud.urls')),
    path('admin/', admin.site.urls),
]
