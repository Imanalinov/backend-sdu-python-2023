from django import template

register = template.Library()


@register.filter(name="map")
def get_item(dictionary, key):
    return dictionary.get(key)
