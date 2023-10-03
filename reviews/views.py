from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from reviews.models import *
from django.http import Http404
from .utils import average_rating

def index(request):
    return render(request, 'base.html')


def search_view(request):
    search_query = request.GET.get('serach', '')
    context = {'search_query': search_query}
    return render(request, 'search.html', context)

def book_list(request):
    book = Book.objects.all()
    reviews = []
    for item in book:
        book_reviews = Review.objects.filter(book=item)
        reviews.append((book, book_reviews))
    return render(request, 'book_list.html', {'book': book, 'reviews': reviews})

def book_detail(request):
    pass

def submit_review(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=book_id)
        user = request.user
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        review = Review.objects.create(user=user, book=book, rating=rating, comment=comment)
        return redirect('book_detail', book_id=book_id)
    return HttpResponseBadRequest()