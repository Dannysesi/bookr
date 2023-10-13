from django.contrib import admin
from .models import *

# Register your models here.
# class PublisherAdmin(admin.ModelAdmin):
#     list_display = ['name', 'website', 'email']

# admin.site.register(Publisher, PublisherAdmin)

admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Contributor)
admin.site.register(BookContributor)
admin.site.register(Review)
admin.site.register(Genre)
# admin .site.register(Author)