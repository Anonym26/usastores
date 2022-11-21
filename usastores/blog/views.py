from django.views.generic import ListView, DetailView

from blog.models import *


class BlogHome(ListView):
    model = Blog  # ссылается на модель Blog
    template_name = 'blog/index.html'  # прописываем путь
    context_object_name = 'posts'  # для использования в шаблоне
    paginate_by = 2  # пагинация

    def get_context_data(self, *, object_list=None, **kwargs):
        """Формирует динамический и статический контекст, который передается в шаблон"""
        context = super().get_context_data(**kwargs)  # обращаемся к базовому классу и берем существующий контекст
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        """Возвращает только те записи у которых указанное поле = True"""
        return Blog.objects.filter(is_published=True)



# создаем класс DetailView для отображения поста
class ShowPost(DetailView):
    model = Blog
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        """Формирует динамический и статический контекст, который передается в шаблон"""
        context = super().get_context_data(**kwargs)  # обращаемся к базовому классу и берем существующий контекст
        context['title'] = context['post']
        context['cat_selected'] = 0
        return context


class BlogCategory(ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Blog.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context
