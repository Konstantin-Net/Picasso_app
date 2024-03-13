from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import File
from .serializers import FileSerializer
from .tasks import process_file


class FileUploadView(APIView):
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_instant = file_serializer.save()
            process_file.delay(file_instant.id)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileListView(viewsets.ReadOnlyModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

