from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from groceries_data.forms import GroceriesInfoForm
from groceries_data.models import GroceriesInfo


User = get_user_model()

def home(request):
    context = {}
    groceries = GroceriesInfo.objects.all()
    p = Paginator(groceries, 10)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page()
    context = {'groceries': groceries,
               'page_obj': page_obj}
    return render(request, 'groceries_data/home.html', context)


@login_required
def info(request):
    context = {}
    obj = get_object_or_404(User, id = request.user.id)
    if request.method == "POST":
        form = GroceriesInfoForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.uploader = obj
            form.save()
            messages.success(request, "Data has been created.")
            return redirect('home')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GroceriesInfoForm()
    context['form'] = form
    return render(request, "groceries_data/info.html", context)


@login_required
def update_info(request, id):
    context ={}
    obj = get_object_or_404(GroceriesInfo, id = id)
    form = GroceriesInfoForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        messages.success(request, "Data has been updated.")
        return redirect('home')
        
    context["form"] = form
    return render(request, "groceries_data/update_info.html", context)


@login_required
def delete_info(request, id):
    obj = get_object_or_404(GroceriesInfo, id = id)
    if request.method == "POST":
        obj.delete()
        messages.error(request, "Data has been deleted.")
        return redirect('home')
    context = {'obj': obj}
    return render(request, "groceries_data/delete_info.html", context)