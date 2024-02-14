from django.urls import path
from .views import BookCreateView, ContributorCreateView, BookUpdateView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('book_detail/<int:id>/', views.book_detail, name='book_detail'),
    path('book/new/', BookCreateView.as_view(), name='book-create'),
    path('book/new/contributor', ContributorCreateView.as_view(), name='contributor-create'),
    path('book_detail/<int:pk>/update/', BookUpdateView.as_view(), name='book-update')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)