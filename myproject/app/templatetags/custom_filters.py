from django import template

register = template.Library()

@register.filter
def dynamic_attribute(obj, attr_name):
    return getattr(obj, attr_name, '')

@register.filter
def get_fields(obj):
    return [field.name for field in obj._meta.get_fields()]
