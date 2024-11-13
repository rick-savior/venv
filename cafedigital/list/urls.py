from rest_framework.routers import DefaultRouter
from list.views import CafésViewSet

app_name = 'list'

router = DefaultRouter(trailing_slash=False)
router.register(r'list', CafésViewSet)

urlpatterns = router.urls