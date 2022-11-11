from django.urls import re_path, path
from . import views
from .views import *

app_name = 'shop'

# список маршрутов текущего приложения
urlpatterns = [
    path('', product_list, name='product_list'),
    path('product_list/<slug:category_slug>',
         product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>',
         views.product_detail,
         name='product_detail'),
]
