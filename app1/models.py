from django.db import models

# Create your models here.

class Books(models.Model):
    book_name=models.CharField(max_length=200,primary_key=True)
    def __str__(self):
        return self.book_name
class Book_Details(models.Model):
    book_name=models.ForeignKey(Books,on_delete=models.CASCADE)
    price=models.IntegerField()
    book_auth_name=models.CharField(max_length=200)
    def __str__(self):
        return self.book_name
        
        
    
class Books_store(models.Model):
    books_store_name=models.CharField(max_length=200)
    book_name=models.ForeignKey(Book_Details,on_delete=models.CASCADE)
    date=models.DateField()
    def __str__(self):
        return self.books_store_name
        
    
    
