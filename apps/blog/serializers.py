from rest_framework import serializers

from .models import Tag, Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            'title',
            'body',
            'likes',
            'slug',
            'created_at',
            'updated_at'
        )


class TagSerializer(serializers.ModelSerializer):
    blogs = BlogSerializer(many=True)

    class Meta:
        model = Tag
        fields = (
            'title',
            'slug',
            'description',
            'blogs'
        )
