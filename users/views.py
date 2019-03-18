from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Contact


# Create your views here.
class ContactListView(ListView):
    model = Contact
    context_object_name = 'contacts'
    template_name = 'users/index.html'
    ordering = ['name']


class ContactCreateView(CreateView):
    model = Contact
    fields = ['name', 'email', 'telephone', 'relation', 'residence', 'cover', 'is_male']
    template_name = 'users/create_contact.html'


class ContactUpdateView(UpdateView):
    model = Contact
    fields = ['name', 'email', 'telephone', 'relation', 'residence', 'cover', 'is_male']
    template_name = 'users/create_contact.html'


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = '/'

