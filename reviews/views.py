from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name = 'world'
    return render(request, 'base.html', {'name': name})

def search(request):
    return render(request, 'search.html')


def search_view(request):
    # Step 2: Read the search string from URL parameters
    search_query = request.GET.get('q', '')

    # Step 3: Pass the search value to the template
    context = {'search_query': search_query}

    # Step 4: Render the template with the context
    return render(request, 'search.html', context)