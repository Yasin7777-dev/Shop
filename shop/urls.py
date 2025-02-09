from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from products.schema import schema
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('admin/', admin.site.urls),
    
   path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)