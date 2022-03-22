from rest_framework import generics

from .serializers import BlogSerializer, TagSerializer
from .models import Tag, Blog


class BlogListAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BLogRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'slug'


class TagListAPIView(generics.ListAPIView):
    queryset = Tag.objects.prefetch_related('blogs')
    serializer_class = TagSerializer
