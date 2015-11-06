from django.shortcuts import render,redirect
from .models import List, Todo, User
# Create your views here.
from .forms import AddToList, AddToTodo, ChangeList, ChangeTodo
from itertools import chain

def index(request):
    # if request.user.is_authenticated:
    #     print "User is logged in"
    #     response = {}
    #     response.update(get_owners_list(request))
    #     return render(request, 'todo/index.html',response)
    # else:
    #     print "please log in"
    response = {}
    if request.user.is_authenticated():
        response = get_list_and_todos(request)
    return render(request,'index.html',response)


# HTML VIEWS

def view_lists(request):
    response = get_owners_list(request)
    return render(request,'todo/view_collection.html',response)

def view_todo(request):
    response = get_todos(request)
    return render(request, 'todo/view_tasks.html',response)

def view_list_form(request):
    check_user(request)
    return render(request, 'todo/add_collections.html')

## html render for todos is done by create_todo



## View existing lists and todos

def get_list_and_todos(request):
    user = User.objects.get(pk=request.user.id)


    #lists = []
    todos = []
    lists = List.objects.filter(owner=user)
    for list in lists:
        todo_set = Todo.objects.filter(list=list)
        for todo in todo_set:
            todos.append(todo)

    print lists, todos
    response = { 'lists': lists,
                 'todos':todos,
               }
    return response

def get_owners_list(request):
    user = User.objects.get(pk=request.user.id)
    lists = List.objects.filter(owner=user)
    response = {
        'lists': lists,
    }
    return response

def get_todos(request):
    user = User.objects.get(pk=request.user.id)
    lists = List.objects.filter(pk=user.id)
    todos = []
    for list in lists:
        items = Todo.objects.filter(list=list)
        todos = chain(todos,items)
    response = {
        'todos':todos,
    }
    return response

## Creating list and todo views


def create_list(request):
    if request.method == 'POST':
        print "Heard a post request"

def create_list(request):
    if request.method == 'POST':
        try:
            form = AddList(request.POST)
            if form.is_valid():
                print "Able to create a new list"
                form.save()
                return index(request)
            else:
                print form.errors
        except Exception:
            print "Something went wrong"


def create_todo(request,id):
    if request.method == "GET":
        list = List.objects.get(pk=id)
        response = {'list':list}
        return render(request, 'todo/add_tasks.html',response)

    if request.method == 'POST':
        try:
            list = List.objects.get(pk=id)
            print list
            form = AddTodo(request.POST)
            if form.is_valid():
                print "Able to create a new todo"
                form.save()
                return index(request)
            else:
                print form.errors
        except Exception:
            print "Something went wrong"

def complete_todo(request,id):
    print "setting todo to complete/incomplete"
    todo = Todo.objects.get(pk=id)
    if todo.completed == True:
        todo.completed = False
    else: 
        todo.completed = True
    todo.save()
    print todo.completed
    return redirect('index')

## Deleting lists and todos

def delete_list(request,id):
    user = request.user
    try:
        list = List.objects.get(pk=id)
        if user == list.user:
            list.delete()
        else:
            print "you don't have access to this"
    except Exception:
        print "something went wrong"
    return redirect('index')

def delete_todo(request,id):
    try:
        todo = Todo.objects.get(pk=id)
        print "deleting todo"
        todo.delete()
    except Exception:
        print "Todo could not be deleted"
    return redirect('index')

 ## Editing lists and Todos

def edit_list_form(request, id):
    check_user(request)
    try:
        list = List.objects.get(pk=id)
        response = {
        'list':list,
        }
        return render(request, 'todo/edit_collections.html', response)
    except Exception:
        print "Something went wrong"

def edit_todo_form(request, id):
    try:
        lists = get_owners_list(request)
        todo = Todo.objects.get(pk=id)
        response = {
        'todo':todo,
        'lists':list,
        }
        return render(request, 'todo/edit_tasks.html', response)
    except Exception:
        print "Something went wrong"


def edit_list(request,id):
    if request.method == 'POST':
        try:
            list = List.objects.get(pk=id)
            print list
            form = changeList(request.POST, list=list)
            if form.is_valid():
                print "Able to create a new list"
                form.save()
                return index(request)
            else:
                print form.errors
        except Exception:
            print "Something went wrong"


def edit_todo(request,id):
    if request.method == 'POST':
        try:
            todo = Todo.objects.get(pk=id)
            print todo
            form = ChangeTodo(request.POST, todo=todo)
            if form.is_valid():
                print "Able to create a new todo"
                form.save()
                return index(request)
            else:
                print form.errors
        except Exception:
            print "Something went wrong"



def check_user(request):
    if not request.user.is_authenticated():
        return redirect('index.html')