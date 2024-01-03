from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from dogs.models import Category, Dog


class IndexView(TemplateView):
    template_name = 'dogs/index.html'
    extra_context = {
        'title': 'Питомник - Главная'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Category.objects.all()[:3]
        return context_data


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Питомник - все наши породы'
    }



class DogListView(ListView):
    model = Dog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk
        context_data['title'] = f'Собаки породы - {category_item.name}'

        return context_data


class DogCreateView(CreateView):
    model = Dog
    fields = ('name', 'category',)
    success_url = reverse_lazy('dogs:categories')


class DogUpdateView(UpdateView):
    model = Dog
    fields = ('name', 'category',)

    def get_success_url(self):
        return reverse('dogs:category', args=[self.object.category.pk])


class DogDeleteView(DeleteView):
    model = Dog
    success_url = reverse_lazy('dogs:categories')
