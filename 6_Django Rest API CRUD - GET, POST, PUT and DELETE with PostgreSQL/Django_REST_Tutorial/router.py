
from rest_framework import routers
from DjangoRESTApp.viewsets import AdmissionViewSet

router = routers.DefaultRouter()

router.register('admission',AdmissionViewSet,basename="Admission")

urlpatterns = router.urls


