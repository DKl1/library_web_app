from .models import Order
from book.models import Book
from authentication.models import CustomUser
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authentication.decorators import allowed_users
from datetime import datetime, timedelta
from .forms import OderForm


@login_required(login_url='login')
@allowed_users(allowed_roles=['librarian'])
def orders_for_librarian(request):
    orders = Order.get_all()
    context = {'orders': orders}
    return render(request, 'order/orders.html', context)


@login_required(login_url='login')
def orders_for_user(request):
    user = request.user.id
    orders = Order.objects.filter(user__id=user)
    context = {'orders': orders}
    return render(request, 'order/orders.html', context)


# @login_required(login_url='login')
# @allowed_users(allowed_roles=['librarian'])
# def close_order(request, id):
#     order = Order.get_by_id(id)
#     if request.method == "POST":
#         date = request.POST['date']
#         order.update(end_at=date)
#
#     context = {'order': order}
#     return render(request, 'order/close_order.html', context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['librarian'])
def close_order(request, id):
    order = Order.get_by_id(id)

    if request.method == "POST":
        order.update(end_at=datetime.now())
        return redirect('orders')

        # date = request.POST['date']
        # order.update(end_at=date)

    context = {'order': order}
    return render(request, 'order/close_order.html', context)


@login_required(login_url='login')
def create_order(request, book_id,):
    book = Book.get_by_id(book_id)
    user = CustomUser.get_by_id(request.user.id)
    planned_end_at = datetime.today() + timedelta(days=20)

    context = {
        'book': book.name,
        'reader': user.email,
        'planned_end_at': planned_end_at,
               }

    if request.method == "POST":
        try:
            Order.create(user, book, planned_end_at)
            return redirect("books")
        except Exception:
            pass
    return render(request, 'order/create_order.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['librarian'])
def update_order(request, id):
    order = Order.objects.get(id=id)
    print(order)

    if request.method == 'POST':
        order_form = OderForm(request.POST, instance=order)
        if order_form.is_valid():
            order_form.save()
            return redirect('orders')
    else:
        order_form = OderForm(instance=order)

    context = {'form': order_form}
    return render(request, 'order/update_order_form.html', context=context)
