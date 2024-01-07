from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from reviews.models import *
from django.http import Http404
from .utils import average_rating
from .forms import BookSearchForm, BookForm, BookImageForm, ContributorForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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
    genres = Genre.objects.values('genre').distinct()
    return render(request, 'book_list.html', {'books': books, 'genres': genres})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    reviews = Review.objects.filter(book=book)
    return render(request, 'book_detail.html', {'book': book, 'reviews': reviews,})

def submit_review(request, id):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=id)
        creator = request.user  # Corrected line
        rating = request.POST.get('rating')
        content = request.POST.get('comment')
        review = Review.objects.create(creator=creator, book=book, rating=rating, content=content)
        return redirect('book_detail', id=id)
    return HttpResponseBadRequest()



def books_by_genre(request, genre_type):
    books = Book.objects.filter(genre__genre=genre_type)
    return render(request, 'genresort.html', {'genre_type': genre_type, 'books': books})

def contributorsort(request, contributor_name):
    contributors = Contributor.objects.all()
    return render(request, 'book_form.html', {'contributors': contributors})


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_form'] = BookImageForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        image_form = BookImageForm(request.POST, request.FILES)
        
        if form.is_valid() and image_form.is_valid():
            form.instance.author = self.request.user
            form.instance.image = image_form.cleaned_data['image']
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

class ContributorCreateView(CreateView):
    model = Contributor
    form_class = ContributorForm
    template_name = 'reviews/contributor_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_form'] = BookImageForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        image_form = BookImageForm(request.POST, request.FILES)
        if form.is_valid() and image_form.is_valid():
            return self.form_valid(form, image_form)
        else:
            return self.form_invalid(form, image_form)

    def form_valid(self, form, image_form):
        form.instance.author = self.request.user
        self.object = form.save()
        image_form.instance.book = self.object
        image_form.save()
        return super().form_valid(form)

    def form_invalid(self, form, image_form):
        return self.render_to_response(
            self.get_context_data(form=form, image_form=image_form)
        )

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.author:
            return True
        return False

    

