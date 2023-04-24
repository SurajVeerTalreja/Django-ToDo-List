from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Todo
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
def index(request):
    todo_list = Todo.objects.all().order_by('-is_urgent')[:2]
    return render(request, 'todo_list/index.html', {
        'todo': todo_list,
    })


def all_items(request):
    todo_list = Todo.objects.all()
    return render(request, 'todo_list/all-items.html', {
        'todo': todo_list,
    })


class TodoCreateView(CreateView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('home-page')


def item_detail(request, slug):
    selected_item = Todo.objects.get(slug=slug)
    return render(request, 'todo_list/item_detail.html', {
        'item': selected_item
    })


def delete_item(request, slug):
    item_to_delete = Todo.objects.get(slug=slug)
    item_to_delete.delete()
    messages.success(request, 'The Activity has been deleted successfully! Remaining Activities will upload in a second!')
    return redirect('all-items')
