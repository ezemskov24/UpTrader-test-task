from typing import Dict, Any, List

from django import template

from ..models import Menu


register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name) -> Dict[str, Any]:
    """
    Возвращает отрисованный шаблон меню для указанного имени меню
    """
    menu_items = Menu.objects.filter(name=menu_name, parent__isnull=True).prefetch_related('children__children')
    menu_tree = build_menu_tree(menu_items)
    return {
        "menu_tree": menu_tree,
    }


def build_menu_tree(menu_items) -> List[Dict[str, Any]]:
    """
    Строит древовидное представление меню на основе списка элементов меню
    """
    menu_tree = []
    for item in menu_items:
        children = build_menu_tree(item.children.all())
        menu_tree.append({
            'item': item,
            'children': children
        })
    return menu_tree
