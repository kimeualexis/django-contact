from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Contact
from django.contrib.auth.mixins import LoginRequiredMixin
from . forms import UserForm
from django.contrib.auth import authenticate, login


# Create your views here.
class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
    context_object_name = 'contacts'
    template_name = 'users/index.html'
    ordering = ['name']

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)


class ContactCreateView(CreateView):
    model = Contact
    fields = ['name', 'email', 'telephone', 'relation', 'residence', 'cover', 'is_male']
    template_name = 'users/create_contact.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ContactUpdateView(UpdateView):
    model = Contact
    fields = ['name', 'email', 'telephone', 'relation', 'residence', 'cover', 'is_male']
    template_name = 'users/create_contact.html'


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = '/'


def user_signup(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('users:contact-index')
    return render(request, 'registration/register.html', {'form': form})


