from .models import Contact
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy


class ContactListView(ListView):
    model = Contact
    template_name = 'contact_list.html'


class ContactCreateView(CreateView):
    model = Contact
    fields = '__all__'
    template_name = 'contact_cu.html'
    success_url = reverse_lazy('contact_list')


class ContactUpdateView(UpdateView):
    model = Contact
    fields = '__all__'
    template_name = 'contact_cu.html'
    success_url = reverse_lazy('contact_list')


class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'contact_delete.html'
    success_url = reverse_lazy('contact_list')


class ContactDetailView(DetailView):
    model = Contact
