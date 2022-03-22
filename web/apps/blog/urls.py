from django.urls import path

from .views import BlogListAPIView, BLogRetrieveAPIView, TagListAPIView


urlpatterns = [
    path('blogs/', BlogListAPIView.as_view(), name='blogs'),
    path('blogs/<slug:slug>/', BLogRetrieveAPIView.as_view(), name='blog-detail'),
    path('tags/', TagListAPIView.as_view(), name='tags'),
]
