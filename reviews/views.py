from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from reviews.models import *
from django.http import Http404
from .utils import average_rating
from .forms import BookSearchForm

def base(request):
    return render(request, 'base.html')


def book_search(request):
    if 'query' in request.GET:
        query = request.GET['query']
        results = Book.objects.filter(title__icontains=query)
    else:
        results = None

    form = BookSearchForm()

    return render(request, 'search.html', {'results': results, 'form': form})

def book_list(request):
    books = Book.objects.all()
    genres = Genre.objects.all()
    return render(request, 'book_list.html', {'books': books, 'genres': genres})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    # role = get_object_or_404(BookContributor, id=id)
    reviews = Review.objects.filter(book=book)
    return render(request, 'book_detail.html', {'book': book, 'reviews': reviews,})

def submit_review(request, id):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=id)
        creator = request.user  # Corrected line
        rating = request.POST.get('rating')
        content = request.POST.get('comment')  # Corrected line (changed 'content' to 'comment')
        review = Review.objects.create(creator=creator, book=book, rating=rating, content=content)
        return redirect('book_detail', id=id)
    return HttpResponseBadRequest()



def books_by_genre(request, genre_type):
    books = Book.objects.filter(genre__genre=genre_type)
    return render(request, 'genresort.html', {'genre_type': genre_type, 'books': books})


