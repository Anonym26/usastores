from .cart import Cart


def cart(request):
    """
    Получает объект запроса и возвращает словарь объектов,
    которые будут доступны всем шаблонам, визуализированным
    с помощью RequestContext
    """
    return {'cart': Cart(request)}
