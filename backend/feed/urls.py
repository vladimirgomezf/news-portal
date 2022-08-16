from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('auth/', include('rest_framework.urls')),

    path('news/', NewsList.as_view()),
    path('news/<int:pk>/', NewsDetail.as_view()),

    path('logs/', LogRegistryList.as_view()),
    path('logs/<int:pk>/', LogRegistryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
