from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    print('*'*50)
    print('the blog route is working')
    return HttpResponse('placeholder to later display a list of all blogs')

def new(request):
    print('*'*50)
    print('the new route is working')
    return HttpResponse('placeholder to display a new form to create a new blog')

def create(request):
    print('*'*50)
    print('the create route is working')
    return redirect('/blogs')

def show(request, number):
    print('*'*50)
    print('the show route is working')
    return HttpResponse(f'placeholder to display blog number:{number}')

def edit(request, number):
    print('*'*50)
    print('the edit route is working')
    return HttpResponse(f'placeholder to edit blog number:{number}')

def destroy(request, number):
    print('*'*50)
    print('the destroy route is working')
    return redirect('/blogs')