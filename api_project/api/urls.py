from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('books/', BookList.as_view(), name='book-list'),
    path('api-auth/', include('rest_framework.urls')),
]
