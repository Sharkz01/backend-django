from rest_framework import serializers
from .models import PostJob

class PostJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostJob
        fields = ('pk', 'title', 'image', 'company', 'link', 'post', 'description', 'agency')