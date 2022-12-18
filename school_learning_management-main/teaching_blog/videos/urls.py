from django.urls import path

from .views import indexes,indexesOne

urlpatterns = [
    path('', indexes),
    path('indexesOne/', indexesOne),
]
