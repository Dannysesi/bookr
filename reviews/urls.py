from django.urls import path
from . import views

urlpatterns = [
    # path('book_list/', views.book_list, name='book_list'),
    path('book_detail/<int:id>/', views.book_detail, name='book_detail'),
    path('book_detail/', views.book_detail, name='book_detail')
]