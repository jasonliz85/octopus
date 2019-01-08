from django.urls import path

from . import views

urlpatterns = [
    path('wordcloud',   views.wordcloud, name='wordcloud'),
    path('wordcloud/admin',       views.admin, name='admin'),
]
