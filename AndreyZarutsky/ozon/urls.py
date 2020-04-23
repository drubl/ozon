from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from django.urls import path
# from rest_framework.schemas import get_schema_view
# from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
#
# schema_view = get_schema_view(
#     title='Ozon vtiss API',
#     renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer]
# )
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Ozon API')

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include auth URLs for the browsable API.
# urlpatterns = [
#     url('', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]
from rest_framework.documentation import include_docs_urls
urlpatterns = [
    path(r'docs/', include_docs_urls(title='Ozon API')),
    url('', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'api-documentation', schema_view),
    path('api/customer/', include('basket.presentation.urls')),
    path('api/customer/', include('customers.presentation.urls')),
    path('api/products/', include('products.presentation.urls')),
    path('api/login', include('auth.presentation.urls')),
    path('api/log', include('auth.presentation.urls')),
    path('admin/', admin.site.urls),
]
