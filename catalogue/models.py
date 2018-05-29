import uuid

from django.db import models
from django.urls import reverse

# Genre class

class Genre(models.Model):
    name=models.CharField(max_length=200, help_text='Enter the book genre (Science Fiction, Journalism, etc.)')
    
    def __str__(self):
        return self.name

# Language class

class Language(models.Model):
    name=models.CharField(max_length=200, help_text='Enter the book\"s natural language (English, French, Swahili, etc.)')
    
    def __str__(self):
        return self.name

# Books class

class Books(models.Model):
    
    '''
    Model representing a book (but not a specific copy of a book). 
    '''
    
    title=models.CharField(max_length=200)
    author=models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign key used because authors can have multiple books (book with multiple authors not yet implemented). 
    # Author declared as a string rather than object because it hasn't been declared in the file yet. 
    summary=models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn=models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre=models.ManyToManyField(Genre, help_text='Select a genre for this book.')
    # ManyToMany used because genre can contain many books. Books can cover many genres. 
    # Genre class has already defined so we can specify the object above. 
    
    def __str__(self):        
        return self.title
    
    def get_absolute_url(self):
        
        '''
        Returns the URL to access a detail record for this book
        '''
        
        return reverse('book-detail', args=[str(self.id)])

# Book Instance class

class BookInstance(models.Model):
    
    '''
    Model representing a specific copy of a book. 
    '''
    
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across the entire library.')
    book=models.ForeignKey('Books', on_delete=models.SET_NULL, null=True)
    imprint=models.CharField(max_length=200)
    due_back=models.DateField(null=True, blank=True)
    
    LOAN_STATUS=(
        ('m', 'Maintenance'), 
        ('o', 'On Loan'), 
        ('a', 'Available'), 
        ('r', 'Reserved'), 
    )
    
    status=models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book Availability')
    
    class Meta:
        ordering=['due_back']
    
    def __str__(self):
        return '{0}, {1}'.format(self.id, self.book.title)

# Author class

class Author(models.Model):
    
    '''
    Model representing an Author. 
    '''
    
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    date_of_birth=models.DateField(null=True, blank=True)
    date_of_death=models.DateField('Died', null=True, blank=True)
    
    class Meta:
        ordering=['first_name', 'last_name']
    
    def get_absolute_url(self):
        
        '''
        Returns the URL to access a particular Author instance. 
        '''
        
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):     
        return '{0}, {1}'.format(self.last_name, self.first_name)

