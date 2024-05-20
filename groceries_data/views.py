from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from groceries_data.forms import GroceriesInfoForm
from groceries_data.models import GroceriesInfo

def home(request):
    context = {}
    groceries = GroceriesInfo.objects.all()
    context['groceries'] = groceries
    print(request.user)
    return render(request, 'groceries_data\home.html', context)


def info(request):
    context = {}
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = GroceriesInfoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            messages.success(request, "Data has been created.")
            return redirect('home')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GroceriesInfoForm()
    context['form'] = form
    return render(request, "groceries_data/info.html", context)


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


def delete_info(request, id):
    obj = get_object_or_404(GroceriesInfo, id = id)
    if request.method == "POST":
        obj.delete()
        messages.error(request, "Data has been deleted.")
        return redirect('home')
    context = {'obj': obj}
    return render(request, "groceries_data/delete_info.html", context)