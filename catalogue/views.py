from django.shortcuts import render

from catalogue.models import Author, Book, BookInstance, Genre

def index(request):
    
    '''View function for the home page.'''
    
    # Generate counts of some of the main objects
    
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    
    # Available books (status='a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    
    # The all() is implied by default
    num_authors=Author.objects.count()
    
    context={
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }
    
    # Render the HTML template with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class BookListView(generic.ListView):
    model=Book

class AuthorListView(generic.ListView):
    model=Author

class BookDetailView(generic.DetailView):
    model=Book

class AuthorDetailView(generic.DetailView):
    model=Author
