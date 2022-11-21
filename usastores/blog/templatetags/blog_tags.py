from django import template
from blog.models import *

register = template.Library()


# включающий тег
@register.inclusion_tag('blog/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    """
    Возвращает список категорий.
    """
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('blog/list_last_post.html')
def show_last_posts():
    """
    Возвращает 3 последних поста.
    """
    posts = Blog.objects.filter(is_published=True).order_by('-id')[:3]
    return {'posts': posts}
