from django.urls import path

from .views import *

# список маршрутов текущего приложения
urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', BlogCategory.as_view(), name='category'),
]
