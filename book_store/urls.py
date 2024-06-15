from django.urls import include, path
from rest_framework import routers
from .views import GenreViewSet, AuthorViewSet, BookViewSet, BookAuthorViewSet

router = routers.DefaultRouter()
router.register(r'genres', GenreViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'books-authors', BookAuthorViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls))
]