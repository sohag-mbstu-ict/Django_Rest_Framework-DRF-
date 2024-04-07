from rest_framework import routers
from Object_Detection_App.viewsets import UploadedFileViewSet
router = routers.DefaultRouter()

router.register('upload_file',UploadedFileViewSet,basename="upload_file")

urlpatterns=router.urls

