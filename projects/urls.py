from rest_framework import routers
from .api import ProjectViewSet

## esto usa un modulo especial para crear todas las rutas basicas

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls