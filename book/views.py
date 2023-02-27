# Create your views here.
from django.shortcuts import render
from .models import *
from django.db.models import Q
from order.models import Order


def books(request):
    list_book = Book.get_all()
    search = request.GET.get('search', '')

    if search:
        list_book = Book.objects.filter(Q(name__icontains=search) | Q(authors__name__icontains=search) |
                                        Q(authors__surname__icontains=search))
    else:
        list_book = Book.get_all()
    context = {'list_book': list_book}
    return render(request, 'book/book.html', context)


# def about(request, id):
#     item = Book.get_by_id(id)
#     if request.method == 'POST':
#         date = request.POST['date']
#         Order.create(request.user, item, date)
#
#     context = {'item': item}
#     return render(request, 'book/about.html', context)

def about(request, id):
    item = Book.get_by_id(id)
    if request.method == 'POST':
        date = request.POST['date']
        Order.create(request.user, item, date)

    context = {'item': item}
    return render(request, 'book/about.html', context)
