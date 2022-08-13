from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BookSerializer
from .models import Books
from booksapi import serializers

# Create your views here.
"""
@api_view(['GET'])
def apiOverView(request):
    booksapi_urls = {
        'List': '/books-list',
        'Detail View': '/books-detail/<int:id>',
        'Create':'/books-create',
        'Update': '/books-update/<int:id>',
        'Delete': '/books-delete/<int:id>',
    }
    return Response(booksapi_urls);

"""

# Show All books
@api_view(['GET'])
def ShowAll(request):
    books=Books.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response (serializer.data)


# Show book of perticular id
@api_view(['GET'])
def ViewBooks(request,pk):
    books=Books.objects.get(id=pk)
    serializer = BookSerializer(books, many=False)
    return Response (serializer.data)


# Create Books details
@api_view(['POST'])
def CreateBooks(request):
    serializer= BookSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


#update by id
@api_view(['POST'])

def UpdateBooks(request,pk):
    books=Books.objects.get(id=pk)
    serializer = BookSerializer(instance=books, data=request.data)
    
    if serializer.is_valid():
        serializer.save()

    return Response (serializer.data)


# Delete by id

@api_view(['GET'])
def DeleteBooks(request,pk):
    books=Books.objects.get(id=pk)
    books.delete()

    return Response("Book Record Is Deleted !!!")
    
    