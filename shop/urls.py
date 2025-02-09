from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from products.schema import schema
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)