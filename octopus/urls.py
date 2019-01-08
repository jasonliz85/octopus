from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('word_cloud.urls')),
    path('admin/', admin.site.urls),
]

