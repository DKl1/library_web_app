from django.shortcuts import render, redirect
from .models import *
from authentication.decorators import allowed_users
from django.contrib.auth.decorators import login_required
from book.models import Book
from django.http import HttpResponse
from .forms import AuthorForm


@login_required(login_url='login')
@allowed_users(allowed_roles=['librarian'])
def author_page(request):
    authors = Author.get_all()
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        patronymic = request.POST['patronymic']
        Author.create(name, surname, patronymic)

    context = {'authors': authors}
    return render(request, 'author/authors.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['librarian'])
def delete_author(request, id):
    author = Author.get_by_id(id)
    book = Book.objects.filter(authors__id=author.id)

    if book:
        return HttpResponse('This author cant be deleted')
    else:
        if request.method == "POST":
            Author.delete_by_id(author.id)
            return redirect('authors')
        context = {"author": author}
        return render(request, 'author/delete_author.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['librarian'])
def create_author(request):

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors')
    else:
        form = AuthorForm()

    context = {'form': form}
    return render(request, 'author/create_author.html', context=context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['librarian'])
def update_author(request, id):
    author = Author.objects.get(id=id)

    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('authors')

    else:
        form = AuthorForm(instance=author)

    context = {'form': form}
    return render(request, 'author/create_author.html', context=context)





