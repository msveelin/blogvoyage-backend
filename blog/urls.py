from django.urls import path
from . import views
from .views import FileUploadView
urlpatterns = [
    path('api/get_image_urls/', views.get_image_urls, name="get_image_urls"),
    path('api/posts/', FileUploadView.as_view(), name='file-upload'),
    # path('api/posts/', PostCreateView.as_view(), name='post-create'),
]