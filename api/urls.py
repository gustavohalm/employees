from rest_framework import routers
from .views import EmployeViewSet


router = routers.DefaultRouter()
router.register('employe', EmployeViewSet)

urlpatterns = router.urls
