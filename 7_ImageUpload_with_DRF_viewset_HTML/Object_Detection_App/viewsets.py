from django.http import FileResponse
from rest_framework import viewsets
from rest_framework.response import Response
from .models import UploadedFile
from .serializers import UploadedFileSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class UploadedFileViewSet(viewsets.ModelViewSet):
    serializer_class = UploadedFileSerializer
    queryset = UploadedFile.objects.all()
    parser_classes = (MultiPartParser, FormParser)

    

    # def uploaded_files_view(request):
    #     uploaded_files = UploadedFile.objects.all()
    #     return render(request, 'uploaded_files.html', {'uploaded_files': uploaded_files})
    

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     file_path = instance.file.path
    #     response = FileResponse(open(file_path, 'rb'), content_type='video/mp4')
    #     return response
