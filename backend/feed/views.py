from django.views.decorators.csrf import csrf_exempt

from .models import *
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions


class NewsList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @csrf_exempt
    def get(self, request, format=None):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @csrf_exempt
    def get_object(self, pk):
        try:
            return News.objects.get(pk=pk)
        except News.DoesNotExist:
            raise Http404

    @csrf_exempt
    def get(self, request, pk, format=None):
        news = self.get_object(pk)
        serializer = NewsSerializer(news)
        return Response(serializer.data)

    @csrf_exempt
    def put(self, request, pk, format=None):
        news = self.get_object(pk)
        serializer = NewsSerializer(news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def delete(self, request, pk, format=None):
        news = self.get_object(pk)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LogRegistryList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @csrf_exempt
    def get(self, request, format=None):
        logs = LogRegistry.objects.all()
        serializer = LogRegistrySerializer(logs, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = LogRegistrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogRegistryDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @csrf_exempt
    def get_object(self, pk):
        try:
            return LogRegistry.objects.get(pk=pk)
        except LogRegistry.DoesNotExist:
            raise Http404

    @csrf_exempt
    def get(self, request, pk, format=None):
        logs = self.get_object(pk)
        serializer = LogRegistry(logs)
        return Response(serializer.data)

    @csrf_exempt
    def put(self, request, pk, format=None):
        logs = self.get_object(pk)
        serializer = LogRegistrySerializer(logs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def delete(self, request, pk, format=None):
        logs = self.get_object(pk)
        logs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

