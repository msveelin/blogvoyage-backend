from django.shortcuts import render
from django.http import JsonResponse
from .models import Post
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import save_uploaded_file

# Create your views here.
def get_image_urls(request):
    image_urls = Post.objects.values_list('featured_image', flat=True)
    return JsonResponse({'image_urls': list(image_urls)})

class FileUploadView(APIView):
    def post(self, request, *args, **kwargs):
        uploaded_file = request.FILES.get('file')
        if uploaded_file:
            file_path = save_uploaded_file(uploaded_file)
            return Response({'file_path': file_path})
        else:
            return Response({'error': 'NNo file uploaded'}, status=400)