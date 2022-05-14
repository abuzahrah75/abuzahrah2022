from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from core.todo import todos

# Create your views here.
def index(request):
    res_todos = []
    for i in todos:
        res_todos.append(i)
    return render(request, 'tugasan/index.html', {'todos': res_todos})
    # return render(request, 'tugasan/index.html')
