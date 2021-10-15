from django.shortcuts import render
from django.views.generic.list import ListView
from .models import UsersID


class UsersListView(ListView):

    model = UsersID
    template_name = 'users/users_list.html'
    context_object_name = 'users'


