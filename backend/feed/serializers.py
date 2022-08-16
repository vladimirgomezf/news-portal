from rest_framework import serializers
from .models import News, LogRegistry


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['author', 'head', 'resume', 'content']


class LogRegistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogRegistry
        fields = ['method', 'url', 'response']
