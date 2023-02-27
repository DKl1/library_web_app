# Create your views here.
from django.shortcuts import render, redirect
from .models import CustomUser, CustomUserManager
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from order.models import Order
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users
from .forms import CustomUserForm, AuthForm


def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'authentication/register.html', context)


def login_page(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            user = CustomUser.get_by_email(
                email=form.cleaned_data['email']
            )

            if user.is_superuser:
                try:
                    admin = authenticate(email=user.email, password=form.cleaned_data['password'])
                    login(request, admin)
                    return redirect('books')
                except:
                    messages.error(request, f'ERROR! Incorrect password!')
            else:
                if user.password == form.cleaned_data['password']:
                    login(request, user)
                    messages.success(request, f'Success! You are logged in!')
                    return redirect('books')
                else:
                    messages.error(request, f'ERROR! Incorrect password!')
    else:
        form = AuthForm()

    context = {'form': form}
    return render(request, 'authentication/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['librarian'])
def users_page(request):
    users = CustomUser.get_all()
    context = {'users': users}
    return render(request, 'authentication/users.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['librarian'])
def about_user(request, id):
    user = CustomUser.get_by_id(id)

    orders = Order.objects.filter(user__id=user.id)
    context = {'user': user, 'orders': orders}
    return render(request, 'authentication/about_user.html', context)
