from django.shortcuts import render
from django.http import HttpResponse
from app1.models import *
# Create your views here.

def index(request):
    return HttpResponse("<h1>inside index page..</h1>")



def insert_books(request):
    bn=input("enter book name: ")
    B=Books.objects.get_or_create(book_name=bn)[0]
    B.save()
    return HttpResponse("<h1>books insertted....</h1>")
    
    
def insert_book_details(request):
    bn=input("enter book name: ")
    p=int(input("enter price of book: "))
    ba=input("book auther name: ")
    B=Books.objects.get_or_create(book_name=bn)[0]
    BD=Book_Details.objects.get_or_create(book_name=B,price=p,book_auth_name=ba)[0]
    BD.save()
       
    return HttpResponse("<h1>bookss details inserte......</h1>")
    
    
    
def insert_book_store(request):
    bn=input("enter book name: ")
    p=int(input("enter price of book: "))
    ba=input("book auther name: ")
    bsn=input("enter book store name: ")
    d=input("enter date: ")
    B=Books.objects.get_or_create(book_name=bn)[0]
    BD=Book_Details.objects.get_or_create(book_name=B,price=p,book_auth_name=ba)[0]
    BST=Books_store.objects.get_or_create(book_name=BD,books_store_name=bsn,date=d)[0]
    BST.save()    
    return HttpResponse("<h1>bookstore insertted .....</h1>")
    