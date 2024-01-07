from django.db import models
from django.contrib import auth
from PIL import Image
from django.urls import reverse

# Create your models here.
class Publisher(models.Model):
    '''A company that publishes books'''
    name = models.CharField(max_length=50, help_text = 'the name of the publisher',)
    website = models.URLField(help_text="the publisher's website.")
    email = models.EmailField(help_text="the publisher's email address")
    def __str__(self):
        return self.name

class Book(models.Model):
    '''A published book'''
    title = models.CharField(max_length=70, help_text='the title of the book')
    author = models.CharField(max_length=70, help_text='author of the book', null=True)
    publication_date = models.DateField(verbose_name='date the book was published', null=True)
    isbn = models.CharField(max_length=20, verbose_name='the isbn number of the book', unique=True, null=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, null=True)
    contributors = models.ManyToManyField('Contributor', through='BookContributor')
    image = models.ImageField(default='no_image.JPEG', upload_to='book_images', null=True, blank=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'id': self.id})

class Contributor(models.Model):

    first_names = models.CharField(max_length=50, help_text='the contributors first names')
    last_names = models.CharField(max_length=50, help_text='the contributors last name')
    email = models.EmailField(help_text='the contributors email')
    def __str__(self):
        return self.first_names

    def get_absolute_url(self):
        return reverse('book-create')

class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = 'AUTHOR', 'author'
        CO_AUTHOR = 'CO_AUTHOR', 'co_author'
        EDITOR = 'EDITOR', 'editor'

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name='the role this contributor had in the book', choices=ContributionRole.choices, max_length=20)

class Review(models.Model):
    content = models.TextField(help_text='the review text')
    rating = models.IntegerField(help_text='the rating the reviewer has given')
    date_created = models.DateTimeField(auto_now_add=True,
        help_text='the date and time the review was created'
    )
    date_edited = models.DateTimeField(null=True, help_text='the date and time the review was last edited')
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, help_text='the book that this review is for')

class Genre(models.Model):
    class GenreType(models.TextChoices):
        Horror = 'HORROR', 'horror'
        Comedy = 'COMEDY', 'comedy'
        Romance = 'ROMANCE', 'romance'
        Action = 'ACTION', 'action'
        Sci_Fi = 'SCI-FI', 'sci-fi'
        science ='SCIENCE', 'science'

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.CharField(verbose_name='the genre of this book', choices=GenreType.choices, max_length=20)



