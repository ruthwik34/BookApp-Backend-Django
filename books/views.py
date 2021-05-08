from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import BookForm
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import BookSerializer
from django.http.response import JsonResponse
# Create your views here.

# API METHODS


@csrf_exempt
def BookAPI(request, id=0):
    if request.method == 'GET':
        books = Book.objects.all()
        books_serializer = BookSerializer(books, many=True)
        return JsonResponse(books_serializer.data, safe=False)
    # elif request.method == 'POST':
    #     book_data = JSONParser().parse(request)
    #     book_serializer = BookSerializer(data=book_data)
    #     if book_serializer.is_valid():
    #         book_serializer.save()
    #         return JsonResponse("Added Book successfully", safe=False)
    #     return JsonResponse("Failed to add the Book", safe=False)
    # elif request.method == 'PUT':
    #     book_data = JSONParser().parse(request)
    #     # print(book_data)
    #     book = Book.objects.get(id=book_data['id'])
    #     # print(book)
    #     book_serializer = BookSerializer(book, data=book_data)
    #     # print(book_serializer)
    #     if book_serializer.is_valid():
    #         print('hello world')
    #         book_serializer.save()
    #         return JsonResponse("Updated successfully", safe=False)
    #     print(book_serializer.errors)
    #     return JsonResponse("Failed to update", safe=False)
    # elif request.method == 'DELETE':
    #     book = Book.objects.get(id=id)
    #     book.delete()
    #     return JsonResponse("Successfully Deleted", safe=False)
    return JsonResponse("Only Get Method is allowed", safe=False)


@csrf_exempt
def BookDetailsAPI(request, id=0):
    if(request.method == 'GET'):
        obj = Book.objects.get(id=id)
        obj.read_counter = obj.read_counter+1
        obj.save()
        json_obj = Book.objects.filter(id=id).values()
        return JsonResponse(json_obj[0], safe=False)
    return JsonResponse("Try using GET Method", safe=False)


@csrf_exempt
def SortHomePage(request, sort_by):
    if(request.method == 'GET'):
        obj = Book.objects.all().order_by(sort_by)
        obj_serializer = BookSerializer(obj, many=True)
        return JsonResponse(obj_serializer.data, safe=False)
    return JsonResponse("Try using GET Method", safe=False)


def HomePage(request):
    obj = Book.objects.all().order_by('-read_counter')
    context = {
        'object_list': obj
    }
    return render(request, "books/Home.html", context)


def BookDetails(request, pk):
    obj = get_object_or_404(Book, id=pk)
    obj.read_counter = obj.read_counter+1
    obj.save()
    context = {
        "object": obj
    }
    return render(request, "books/Book_details.html", context)
